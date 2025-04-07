Linkerd works by installing a set of ultalight, trasparent "micro-proxies" next to each service instance. Also in Linkerd is possible to have a multicluster approach where the communication pod-to-pod are possible in a federated environment. 
In Linkerd is possible to connect Kubernetes Services across cluster boundaries in a secure, transparent and independent way.
The main features are:
- Unified Trust Domain: Identities of source and destination workloads are validated at every step, both in a and across cluster boundaries
- Separated Failure Domains: If a cluster fails all the other can keep on working
- Support for any type of network
- Observability

![[Pasted image 20250404124508.png]]


Both linkerd and Istio supports sidecar mode, which inject a sidecar along the application container and intecects all the communications for the outside gateway. 
## Sidecar Mode in Linkerd
In Linkerd is possible to decide if the sidecar network should be flat or hierarchical.
In hierarchical mode Linkerd deploys a gateway component on the target cluster that allows it to receive request from the source clusters.

In flat networks each pod can establish a TCP connection to send traffic directly to each other across cluster boundaries, here the gateway is not necessary for data plane traffic, and thanks to this is possible to:
- Reduce Latency
- Reduce operational costs 
- Improve multi-cluster authorization policies

![[Pasted image 20250404124556.png]]