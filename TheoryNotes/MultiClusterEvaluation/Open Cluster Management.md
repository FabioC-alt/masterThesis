OCM is a powerful, modular, extensible platform.
In OCM the approach which is used is the Hub-agent architecture. This architecture is identical to the hub-kubelet from kubernetes.
In this architecture the kubelet is the primary agent node that runs on each node. It can register the node with the apiserver using one of the primary address of the node.

In OCM the function performed by the kubelet are done by the **Klusterlet**
which is also called "managed cluster" or "spoke cluster". The Klusterlet actively pulls the prescription from the hub cluster and reconcile the phsycal Kubernetes clusters.

![[Pasted image 20250403122549.png]]

## [[Hub-Spoke Architecture]]
The benefit of this architecture are the de-coupling most of the multi-cluster operations generally into computation/decision and execution and the actual execution against the target cluster.