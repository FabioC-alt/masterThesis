OCM is a powerful, modular, extensible platform.
In OCM the approach which is used is the Hub-agent architecture. This architecture is identical to the hub-kubelet from kubernetes.
In this architecture the kubelet is the primary agent node that runs on each node. It can register the node with the apiserver using one of the primary address of the node.

In OCM the function performed by the kubelet are done by the **Klusterlet**
which is also called "managed cluster" or "spoke cluster". The Klusterlet actively pulls the prescription from the hub cluster and reconcile the phsycal Kubernetes clusters.
![[Pasted image 20250404125652.png]]

# Workload Management
In OCM is possible to manage multiple cluster using the `ManagedClusterSet` which is a cluster-scoped API in the hub cluster for grouping a few managed clusters into a “set”.

It is possible also to choose to execute more workload from more users using the workspace. Workspace permissions are included the Managed Cluster Set resource. With the help of RBAC is possible to choose who can have access to control a certain workspace and a certain cluster.

For easy access is possible to have two policies to manage a clusterset:

**default:** Any cluster not specifying a ManagedClusterSet will be added into the default

**global:** Here a ManagedClusterSet will include allt the ManagedCluster.

![[Pasted image 20250404130422.png]]
# Hub-Spoke Architecture
The benefit of this architecture are the de-coupling most of the multi-cluster operations generally into computation/decision and execution and the actual execution against the target cluster.

# Cross-Cluster Communication
Networking in OCM is managed through Cluster Proxy, which is an OCM addon to provide L4 network connectivity from hub cluster to managed cluster.

The working principle is based upon the `apiserver-network-proxy` which is a proxy running on both hub cluster and managed clusters.

Network proxy will be established reverse proxy tunnels from a managed cluster to the hub cluster to make clients from the hub network can access the services in the managed cluster’s newtwork.