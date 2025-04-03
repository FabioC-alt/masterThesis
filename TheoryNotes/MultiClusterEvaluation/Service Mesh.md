## [[Istio]]
Istio is a service mesh infrastructure layer that gives application capabilities like zero-trust security, observability and advanced traffic management without code changes. It enables mTLS encryption, policy management and access control.

Istio allows multi-cloud, hybrid and on-prem with a single mesh.

In istio the multicluster-management is splitted using multiple control-plan, each for a different cluster.

To manage the complexity of a service mesh is possible to use Admiral CRDs

# [[Linkerd]]
Linkerd works by installing a set of ultalight, trasparent "micro-proxies" next to each service instance. Also in Linkerd is possible to have a multicluster approach where the communication pod-to-pod are possible in a federated environment. 
In Linkerd is possible to connect Kubernetes Services across cluster boundaries in a secure, transparent and independent way.
The main features are:
- Unified Trust Domain: Identities of source and destination workloads are validated at every step, both in a and across cluster boundaries
- Separated Failure Domains: If a cluster fails all the other can keep on working
- Support for any type of network
- Observability 
![[Pasted image 20250403104525.png]]

Both linkerd and Istio supports sidecar mode, which inject a sidecar along the application container and intecects all the communications for the outside gateway. 

## Sidecar Mode in Linkerd
In Linkerd is possible to decide if the sidecar network should be flat or hierarchical.
In hierarchical mode Linkerd deploys a gateway component on the target cluster that allows it to receive request from the source clusters.

In flat networks each pod can establish a TCP connection to send traffic directly to each other across cluster boundaries, here the gateway is not necessary for data plane traffic, and thanks to this is possible to:
- Reduce Latency
- Reduce operational costs 
- Improve multi-cluster authorization policies

## Sidecar vs Ambient Mode in Istio
Ambient mode in Istio was introduced to overcome the shortcomings of the Sidecar mode. It is based on a two level architecture.

At base level is possible to find the **ztunnel**, also called Zero Trust Tunnel, it is component that aims to power's Istio's ambient data plane mode.
The Ztunnel is responsible for securely connecting and authenticating workloads within the mesh. 

The second layer of the ambient mode is the **Waypoint Proxy** which is a deployment of the [[Envoy]] proxy. The Waypoint Proxy runs outside of the application pod and are completely independent from the application

It is possible to use only the ztunnel if not interested in Authorization, telemetry and Virtual Service Routing

# [[Cilium]]


