# [[Liqo]]
Liqo Service Discovery approach is based upon the DNS-based service discovery. Each cluster is represented as a *ForeignCluster* custom resource.

## Peering
In Liqo to connect two clusters we need to peer them, during the peering procedure is necessary to decide the the amount of resource to share using the _ResourceRequest_ CR, that can be negotiated and accepted by the remote cluster.

Once the request has been accepted the local cluster create a virtual node. The virtual node is necessary to schedule workload.

# [[Karmada]]
In Karamada service discovery is supported using the ServiceImport and ServiceExport CRDs.

To connect the two clusters the remote cluster need to expose a service which can be deployed using the native Kubernetes API. This service is exported by the remote cluster and imported by the local one.

The remote cluster is seen in the local cluster as **derived service** which can be accessed to perform operation and control the status of the control plane on the remote cluster. The request for connection is performed using a request pod.

This process can be simplified using the MultiClusterIngress API provided in Karmada to import external traffic to services in the member clusters.

In karmada is possible to peer the cluster using both push and pull mode, but with pull mode each modification is effective because the cluster is actually receiving directives from the cluster local.

# [[Open Cluster Management]]
In OCM the registration is managed by the _registrationAgent_ which requires a bootstrap kubeconfig.

The agent will create a `ManagedCluster` bootstrap into the hub cluster and a CertificateSigningRequest. The cluster will be accepted by the hub control plane if some requirements are met:

CSR is approved along with the ManagedCluster resource.

![[image.png]]

In OCM is possible to manage multiple cluster using the `ManagedClusterSet` which is a cluster-scoped API in the hub cluster for grouping a few managed clusters into a “set”.

It is possible also to choose to execute more workload from more users using the workspace. Workspace permissions are included the Managed Cluster Set resource. With the help of RBAC is possible to choose who can have access to control a certain workspace and a certain cluster.

For easy access is possible to have two policies to manage a clusterset:

**default:** Any cluster not specifying a ManagedClusterSet will be added into the default

**global:** Here a ManagedClusterSet will include allt the ManagedCluster.