Toward a high availability cloud: Techniques and challenges
https://ieeexplore.ieee.org/abstract/document/6264687?casa_token=R0ZiiW_kZz8AAAAA:Bf86ydrh6eb4N_xTu0PvOOEQOjrNCoSF4IIS_rY42rk43IVZZRbryAxwnmS4y1hqAjcG47fT


High-availability clusters: A taxonomy, survey, and future directions
https://www.sciencedirect.com/science/article/pii/S0164121221002806?casa_token=Jp6iCx9MkUUAAAAA:q50XpNekaUFOUsc4SDz6atxHKke7LLSAWfLZ0iT49olGQJRZSFjPxpSK4w9mZOsv2_H4dD9udg
# High Availability in Cloud
## Key Concepts and Terminology
The ISO/IEC 25010 standard defines as the "*degree to which a system, product or component is operational and accessible when required for use*".

Availability is calculated as the ratio between the time over which the system was observed. Equivalently, availability can be computed as the ratio between the *mean time between failures*, MTBF and the sum of the mean time between failures and the mean time to recover after failures.


# Availability in the cloud: State of the art
https://www.sciencedirect.com/science/article/pii/S1084804515002878?casa_token=Db-Jp6fhqzgAAAAA:nzSrg1IYg0EtvI6SCmbf9crpP7_3w-iGxNSUiqj4tU-Wr2yYARsi4ltqwq21lLBkf6-o1SHhCQ

Availability is a non-functional requirement specified in terms of the percentage of a system or a service is accessible. This percentage determines the allowed outage time for a given period.
High Availability(HA) is a strict requirement and refers to an availability of at least 99.999% of the time, which is approximately 5mins every year.

 However each cloud provider defines availability from
its own technological perspective and provides architectural
solutions and services based on specific definitions. These different
definitions use similar terms but with different interpretations and
measures.
Furthermore, many research papers relate availability to other characteristics of the cloud, such as performance, scalability, elasticity and security; they do not
propose a comprehensive solution that would guarantee availability in the cloud.

This paper surveys current availability solutions in cloud pro-
viders' practices, and those proposed in research papers from the
academia and the industry. For this purpose, we first define a
taxonomy inspired by the Service Availability Forum (SA Forum)
(Toeroe and Tam, 2012) concepts and mechanisms to set the
baseline for the evaluation. 

The TL 9000 Quality Management System
from the QuEST Forum (QuEST Forum, 2010) for the information
and communication industry defines availability as “The prob-
ability that the system is operational when required” and it is
calculated by system uptime over the total time required to be
operational.

![[Pasted image 20250509162900.png]]
One can view the availability of a system through the avail-
ability of its services. Service availability can be defined as:
![[Pasted image 20250509163028.png]]


We talk about HA if a system or a service is available at least
99.999% (a.k.a. five nines) of the time, which allows for a max-
imum of five minutes and 15seconds downtime per year 

Cloud providers consider availability within the context of a
Service Level Agreement (SLA).

![[Pasted image 20250509163555.png]]

# High Availability in Kubernetes
There are two options for configuring the topology of an High Availability in Kubernetes clusters:
- Stacked control plane
- External etcd nodes

## Stacked etcd Topology
A stacked HA cluster is a topology where the distributed data storage cluster provided by etcd is stacked on top of the cluster formed by the nodes managed by kubeadm that run control plane components.

![[Pasted image 20250509180356.png]]

# High Availability Installation Overview in Karmada
 https://karmada.io/docs/installation/ha-installation/

## Etcd HA
This documentation explain high availability for Karmada. The Karmada high availability architecture is very similar to the Kubernetes high availaibility architecture. 

Deploying Karmada in a HA (High Availaibility) environment we can create multiple Karmada API server instead of using a single API server. So even if a Karmada control plane goes down.

Karmada uses two options for configuring the topology of the highly available Karmada cluster.

It is possible to set-up an HA cluster:
- With stacked control plane nodes, where etcd nodes are colocated with control plane nodes
- With external etcd nodes, where etcd runs on separate nodes from the control plane.

### Stacked etcd topology
A stacked HA cluster is a topology where the distributed data storage cluster provided by etcd is stacked on top of the Karmada control plane nodes.

Each control plane node runs an instance of the Karmada API server, Karmada scheduler and Karmada control manager. The Karmada API server can communicate with multiple member cluster, and these member clusters can be registered to the multiple Karmada API servers.

This topology couples the control plane and etcd members on the same nodes. It is simpler set up than a cluster with external etcd nodes and simple to manage for replication.

Therefore a suggested number of minimal cluster is three.

![[Pasted image 20250509174401.png]]
#### Stacked HA Topology

In the **stacked** topology:

- Each **control plane node** runs both:
    
    - the **Kubernetes control plane components** (`kube-apiserver`, `controller-manager`, `scheduler`)
        
    - and a **local `etcd` instance**
        
- All `etcd` instances form a **cluster** across the control plane nodes.
    

#### ✅ Pros:

- Simpler to deploy and maintain.
    
- Fewer machines needed (better for resource-constrained environments).
    
- Easier setup with tools like `kubeadm`.
    

#### ❌ Cons:

- **Failure domain coupling**: if a node fails, you lose both control plane and `etcd` for that node.
    
- Harder to scale etcd independently from the control plane.

### External etcd Topology
#### External HA Topology

In the **external** topology:

- Control plane nodes **do not run `etcd`**.
    
- A **separate set of nodes** is dedicated to running an **external `etcd` cluster**.
    

#### ✅ Pros:

- **Failure domain isolation**: losing a control plane node doesn't affect `etcd`, and vice versa.
    
- Easier to scale and manage `etcd` independently.
    
- Better suited for large, production-grade environments.
    

#### ❌ Cons:

- More complex deployment and maintenance.
    
- Requires **more nodes** and coordination.
    
- More moving parts, which can increase operational overhead.
An HA cluster with external etcd is a topology where the distributed data storage cluster provided by etcd is external to the Karmada cluster formed by the nodes that run Karmada control plane components.

Like the stacked etcd topology, each Karmada control  plane node in an external etcd topology runs an instance of the Karmada API server, Karmada scheduler and Karmada controller manager. The Karmada API server is exposed to the member clusters. The etcd members runs on separate hosts and each etcd host communicates with the Karmada API server of each Karmada control plane node.

This topology decouples the Karmada control plane and the etcd member. It therefore provides an HA setup where losing a control plane instance or an etcd member has less impact and does not affect the cluster redundancy as much as the stacked HA topology.

This topology requires twice the number of hosts as the stacked HA topology. A minimum of three hosts for control plane nodes and three hosts for etcd nodes are required for an HA cluster with external etcd topology.

![[Pasted image 20250509175511.png]]

### Failover Overview
https://karmada.io/docs/next/userguide/failover/failover-overview/

When acting in multi-cluster scenarion, user workload may be deployed in multiple clusters to improve service high availability. In Karmada when a cluster fails or the user does not want to continue running workloads on a cluster, the cluster status will be marked as unavailable and some taints will be added.

The taint-manager will evict workloads from the fault cluster. And then the evicted workloads will be executed on another cluster that is the best-fit.

# High Availability in Liqo
https://docs.liqo.io/en/v1.0.0/usage/service-continuity.html#servicecontinuityha

Liqo allows to deploy the most critical Liqo components in high availability. This is archieved by deploying multiple replicas of the same component in an **active/passive** fashion. This ensures that, even after eventual pod restarts or node failures, exactly one replica is always active while the remaining ones run on standby.

## Resilience to worker nodes failures

In case the pods runs on the local cluster, they are running on the local node and therefore the lifecycle is managed by the Kubernetes system.

While if instead the crushing node is a in a remote cluster, Liqo grants ShadowPod remote resiliency and in case of unavailability of the local cluster, enforcing the presence of the desired pod without requiring the intervention of the originating cluster.

If a *remote worker* node become *NotReady* the Kuberenetes control plane marks all pods scheduled on that node for deletion, leaving them in *Terminating* state **indefinitely**. By design Liqo does not replace a pod that is offloaded, Terminating and running on a failed node.
So in case of remote worker node failure, the expected workload of a deployment could be less than the expected.

It is possible to configure Liqo to make sure that the expected workload is always running on the remote cluster. Which means that if enabled the Liqo custom controller check for all the offloaded and terminting pods running on *NotReady* nodes. A pod which mactch all condition is force-deleted by the controller.

This way, the ShadowPod controller will enforce the presence of the remote pod by creating a new one on a healthy remote worker node, therefore ensuring the expected number of replicas is actively running on the remote cluster.

