# [[Karmada]]
![[image(1).png]]
In karmada the communication between clusters is possible thanks to MultiCluster Service. To support cross cluster communication is possible to use open source projects like Submariner.

To implement access service across multiple clusters with native service name Karmada introduces multiple controllers to sync the services’s backend EndpointSlice.

First Karmada will collect EndpointSlice resources from all targets clusters, and sync them to the Karmada control plane.

Karmada then will sync the collected EndpointSlice resources to all the target clusters, with attaching the EndpointSlice to the service.

Then when the users access through the service the undelying network will route the request to the backend pods in the multiple clusters.

Karmada exploits a service approach.

# [[Liqo]]
![[image(2).png]]While the communications in the local cluster are possible thanks to the normal epslices, to enable cluster-to-cluster communication is necessary to have the epslice on the local cluster and the then the pod can run on the remote cluster.

The pod that is running on the remote cluster is capable of communicating with the pods present on the local cluster thanks to shadow copies of services and epslices.

Liqo exploit a fabric approach.

# [[Open Cluster Management]]
Networking in OCM is managed through Cluster Proxy, which is an OCM addon to provide L4 network connectivity from hub cluster to managed cluster.

The working principle is based upon the `apiserver-network-proxy` which is a proxy running on both hub cluster and managed clusters.

Network proxy will be established reverse proxy tunnels from a managed cluster to the hub cluster to make clients from the hub network can access the services in the managed cluster’s newtwork.

