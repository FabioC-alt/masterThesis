Karmada is a Kubernetes management system that makes possible to run a cloud-native application managing multiple clusters which runs Kubernetes, so by speaking Kubernetes-native API and providing advanced solutions for scheduling capabilities. 


## [[Service Discovery and Binding]]

To perform Service Discovery on Karmada we need two CRDs, the ServiceImport and the ServiceImport.

ServiceExport expose a Kubernetes service from one cluster to other clusters within a fleet, which makes it accessible across boundaries.

ServiceImport resource represents an imported service from an other cluster.

This two need to be installed in the Karmada control plane.

## Service Deployment

First a service is deployed on a cluster 1.

Then is necessary to export this service in order to make it visible to a cluster 2. On the cluster 2 an import is performed in order to create a connection between the two.

In order to make it visible for the cluster 2 to see the cluster 1 we need a PropagationPolicy which notify the cluster 2 that a cluster 1 is exposing its service for communication.

![[image(2) 1.png]]

From Cluster 2 is possible to see the service on the cluster 1 as a **derived service** which can be accessed for controlling the control plane on the cluster2.

What we perform next is a request from a pod.

# Karmada Control Plane

karmada is based upon the kubernetes api to control the workloads. It consists of three main components:

- Karmada API Server
- Karmada Controller Manager
- Karmada Scheduler
![[image(3).png]]


# Karmada Controller Manager

The Karmada Controller Manager runs various controllers, which watch karmada objects and then talk to the underlying cluster’s API servers to create regular Kubernetes resources.

- Cluster Controller: Attach and manage the clusters in Karmada by creating cluster objects
- Policy Controller: watches PropagationPolicy Objects. When one is added the controller selects a group of resources matching the resourceSelector and create a resourcebinding.
- Binding Controller
- Execution Controller

