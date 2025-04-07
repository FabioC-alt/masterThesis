Karmada is a Kubernetes management system that makes possible to run a cloud-native application managing multiple clusters which runs Kubernetes, so by speaking Kubernetes-native API and providing advanced solutions for scheduling capabilities. 

## Service Discovery and Binding
In Karamada service discovery is supported using the ServiceImport and ServiceExport CRDs.

To connect the two clusters the remote cluster need to expose a service which can be deployed using the native Kubernetes API. This service is exported by the remote cluster and imported by the local one.

The remote cluster is seen in the local cluster as **derived service** which can be accessed to perform operation and control the status of the control plane on the remote cluster. The request for connection is performed using a request pod.

This process can be simplified using the MultiClusterIngress API provided in Karmada to import external traffic to services in the member clusters.

In karmada is possible to peer the cluster using both push and pull mode, but with pull mode each modification is effective because the cluster is actually receiving directives from the cluster local.

## Service Deployment


First a service is deployed on a cluster 1.

Then is necessary to export this service in order to make it visible to a cluster 2. On the cluster 2 an import is performed in order to create a connection between the two.

In order to make it visible for the cluster 2 to see the cluster 1 we need a PropagationPolicy which notify the cluster 2 that a cluster 1 is exposing its service for communication.

![[Pasted image 20250404125301.png]]
From Cluster 2 is possible to see the service on the cluster 1 as a **derived service** which can be accessed for controlling the control plane on the cluster2.

What we perform next is a request from a pod.

# Karmada Control Plane

karmada is based upon the kubernetes api to control the workloads. It consists of three main components:

- Karmada API Server
- Karmada Controller Manager
- Karmada Scheduler

![[Pasted image 20250404125246.png]]

# Karmada Controller Manager

The Karmada Controller Manager runs various controllers, which watch karmada objects and then talk to the underlying cluster’s API servers to create regular Kubernetes resources.

- Cluster Controller: Attach and manage the clusters in Karmada by creating cluster objects
- Policy Controller: watches PropagationPolicy Objects. When one is added the controller selects a group of resources matching the resourceSelector and create a resourcebinding.
- Binding Controller
- Execution Controller


# Communication Between Cluster
![[Pasted image 20250404125408.png]]
In karmada the communication between clusters is possible thanks to MultiCluster Service. To support cross cluster communication is possible to use open source projects like Submariner.

To implement access service across multiple clusters with native service name Karmada introduces multiple controllers to sync the services’s backend EndpointSlice.

First Karmada will collect EndpointSlice resources from all targets clusters, and sync them to the Karmada control plane.

Karmada then will sync the collected EndpointSlice resources to all the target clusters, with attaching the EndpointSlice to the service.

Then when the users access through the service the undelying network will route the request to the backend pods in the multiple clusters.

Karmada exploits a service approach.

# Workload Scheduling
In karmada to schedule the workload we can use either the PropagationPolicy or the ClusterPropagationPolicy where the first is the is the namespace-scoped resource type and the cluster is the cluster-scoped resource type. Using this two resources is possible to schedule the workload either in one namespace or in one clusterfile
