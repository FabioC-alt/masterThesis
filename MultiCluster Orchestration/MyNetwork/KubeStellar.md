KubeStellar manages the workload scheduling using the Workload Definition Spaces, which is a space where the Kubernetes workload is an application that runs on Kubernetes. A workload can be made by a single Kubernetes object or several objects that works together.


In KubeStellar there are abstractions called spaces. This spaces are the main object necessary to manage, control and make possible the communication among clusters.

In KubeStellar to define the workloads that needs to be deployed is used the *Workload Definition Spaces*, while for the managing of the clusters and transport the workloads, the *Inventory and Transport Spaces* is used. 

Then thanks to the `BindingPolicy` is possible to specify what objects and where there should be deployed on the *Workload Execution Clusters*.

## Components

### KubeFlex
In the KubeStellar architecture a component called *KubeFlex* is shipped, this makes possible to provide and manage the Inventory and Transport Spaces. Each cluster appears as a control plane in the KubeFlex hosting cluster.

### KubeStellar Controller Manager
This component instantiate once per *Workload Definition Spaces*, and is responsible for watching the `BindingPolicy` object and match the list of the concrete object  and the list of the concrete cluster, to report from the ITS into the WDS.

### Space Manager
Manages the lifecycle for the spaces

### OCM Cluster Manager
The OCM role in this context is to instantiate once per ITS and synch objects from the ITS to the WECs. 

### OCM Agent
This module registers the WEC to the OCM hub.


![[Pasted image 20250404155006.png]]