Liqo is an open source project that enables dynamic and seamless kubernetes multi-cluster topologies.
## Virtual Node
Liqo leverage the virtual node concept. The virtual node abstraction is implemented using an extended version of the _Virtual Kublet Project_.

Kubelet is the primary node agent and it is responsible for registering the node with the control plane and handling the lifecycle of the pods.

The virtual kubelet replaces a traditional kubelet when the controlled entity is not a physical node, allowing to control arbitrary objects through standard kubernetes APIs.

## Node lifecycle Handling

Continuous Polling to understand if the virtual node failed or it is already present, if not than the workload is scheduled to new nodes (virtual or not).

## Pod lifecycle Handling

Pods are handled using the ShadowPod , S_hadowPod are CR wrapping pod definitions and triggering the remote enforcement logic.
## Resource and Service Reflection

![[Pasted image 20250404124738.png]]

Application A is deployed on the local and remote cluster. On local cluster pods P1 and P2 are running along with their services and EndpointSlices.

While the communications in the local cluster are possible thanks to the normal epslices, to enable cluster-to-cluster communication is necessary to have the epslice on the local cluster and the then the pod can run on the remote cluster.

The pod that is running on the remote cluster is capable of communicating with the pods present on the local cluster thanks to shadow copies of services and epslices.
# NetWork Fabric

Liqo uses a hub and spoke technology where a central hub connects to multiple spoke networks, the hub acts as as a central point for communication and shared services. This approach aims to simplify network management and improving security.

The Liqo network fabric enhance the the kubernetes communications to archive with or without NAT communications.

The fabric natively implements a _hub and a spoke_ topology. The current implementation has three main components. Fist the **network manager**, responsible for the negotiation parameters.

The network manager uses a IP address managment plugin to deal with network conflicts.

The second component is the **gateway.** It is in charge of the setup of the VPN tunnel towards remote clusters. At the moment the current interface is WireGuard. The gateway is also in charge of populating the IP tables.

The third element is the **route controller,** which is a Deamon Set responsible for configuring the appropriate routing entries and possibly the overlay network.

# Storage Fabric

The Liqo **storage fabric** enables the seamless offloading of stateful workload. 
The storage fabric is possible to be created in two different ways:
- **Storage Binding Deferral**: until the first consumer is scheduled onto a given cluster.
- **Data Gravity**: using a set of automatic policies to attract pods in the appropriate cluster. With this approach we ensure that pods are scheduled onto clusters physically hosting the correspondent data.
Under the hood the storage fabric is based upon the **Virtual Storage Class**, which embeds the logic to create the appropriate storage pools. If a new *PersistentVolumClaim* is associated with the virtual storage class and its consumer is bound to a node.
Then if the node is:
- **Virtual**: reflects the logic responsible for creating a remote shadow PVC 
- **Real**: the PVC associated with the Liqo storage class is remapped to a second one, associated with the corresponding real storage class to transparently **provision the request volume**.
## Data Gravity Approach

In the data gravity approach the data attracts the associated workload, this is compliant with ensuring best performance in terms of reduced network traffic and latency but also to enforce storage locality and law regulation respect.

## Deferring Storage Binding

This means the only when a new cosumer is assigned to a given cluster, thus ensuring new storage pools are created in the exact location where their associated workload have been scheduled to.

## Liqo peering and discovery method

### Discovery

DNS-based Service Discovery:

- Unicast DNS → Older, Single Physical Server, Supplying the IP of the searched service.
- Multicast DNS → New, Multiple DNS servers that supply the closest Service.


### Peering
![image(2) 1.png](app://5c18468c9b1a18ce2177651440e228946786/home/fabioc/Documents/MasterThesis/TheoryNotes/MultiClusterEvaluation/Images/image(2)%201.png?1743689445240)

While the communications in the local cluster are possible thanks to the normal epslices, to enable cluster-to-cluster communication is necessary to have the epslice on the local cluster and the then the pod can run on the remote cluster.

The pod that is running on the remote cluster is capable of communicating with the pods present on the local cluster thanks to shadow copies of services and epslices.

Liqo exploit a fabric approach. Once the discovery part has ended, it is possible to peer the cluster B using the ForeignCluster Custom Resource.

To set the cluster B as remote peer is possible to se the flag _outgoing peering=yes.→_ Using policies or manually activating it.

## Traditional certificate peering

### Authentication

The cluster A generates a new private key locally and sends a Certificate Signing Request pre-sharing a token to the remote endpoint. If the authentication is granted, the remote module in the cluster B signs the request and assign to A the bare permissions necessary during the peering establishement procedure, and eventually returning the generated certificate.

## Resource Negotiation

Cluster A starts the negotiation by creating a new _ResourceRequest_ CR locally then the CRDReplicator, which is responsible for the interaction among clusters through the replication of custom resources during the peering establishment, takes action, and replicate the CR to the remote cluster B. Then the cluster B discovers the cluster A thanks to the received request and create the _ForeignCluster_ representation, then performs symmetrical authentication procedure.

The request is analyzed by the cluster B in order to decide whether to accept or refuse the _ResourceRequest._ If positive the B cluster issue a _ResourceOffer CR_ to convey the willingness of sharing a given amount of available resources/services and sends the message back to the cluster A using CRDReplicator.

Once accepted the _ResourceOffer,_ the peering relatioship can be finalized, establishing the inter-cluster network fabric.

The established peering relationship is unidirectional, with A being granted the possibility to leverage the resources offered by B, but not vice versa. However it is possible to reverse the procedure and make B capable of obtaining the same rigths of A on B, thus archeiving bidirectional peering.

# Workload Scheduling
In Liqo there are two different mechanism to schedule the workload:
- First: Admins can enable offloading and choose where to put a specific namespace and selecting a specific subset of remote clusters for the execution of the workload → this it done by scheduling some workload to a virtual node
- Second: Is possible to restrict the elegible targets for each workload based on the requirements