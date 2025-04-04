# Intro

MultiCluster environment are choosen because of many different reason. The idead is to leverage the Kubernetes architecture to enable seamless deployment, scaling and management application in a hybrid or a multi-cloud set-up.

## Benefits of a Kubernetes Multi-Cloud Environment
- **Vendor Independence**
- **Scalability and Flexibility**
- **Resilience and Availability**
- **Cost Optimization**
- **Improved Security**

## Core Components of Kubernetes 
To understand the functioning of a Multi-Cluster architecture based on Kuberntes we first need to look at the overview of one single cluster.
Core components of a Kubernetes cluster are **Control Plane** and **Nodes**. 

### Master Node 
The master node is the node where the Control Plane is executing and is responsible for managing the cluster state, schedule the tasks and maintaining the overall health and functioning of the system.
- **API Server**: Entry point for all the Kubernetes commands and operations. Exposes the Kubernetes API.
- **Scheduler**: It is the component in charge for choosing the best Worker node for executing the workload.
- **Controller Manager**: Ensures that the system stays in the desired state.
- **ETCD**: is a distributed key-value store that holds the configuration data and state of the cluster.

### Worker Node
It is also called the **Node Pool** and it is responsible for running the application workloads. Each worker node contains the necessary services to run pods, including the [[Container Runtime]], a Kubelet and a Proxy.

The Key components of the Worker Node are:
- Kubelet: which is an agent that runs on each worker node and ensures that containers in the pod are running and healthy. It polls the API server to update the state of the node and report if some issues are present.
- [[Container Runtime]]: it is the software responsible for running the containers. Handles the creation and management of containers.
- Kube-proxy: Ensure that the networking for the pods and services is properly configured. Facilitates communications between pods on different nodes and maintains the routing of requests to correct pods.

### Pods
The pods are the smallest and simplest Kubernetes objects. Represent a single instance of a running application. 
The key characteristics of a pod are:
- Multi-Container Pods: Meaning that a pod can host one or more container that shares the same network namespace, storage and other resources.
- Pod IP: Each pod gets its own unique IP address within the cluster, allowing containers in localhost to communicate with each other.
- Ephemeral Nature: Because pods are temporary. When a pod dies or terminate, is possible to make Kubernetes create a new one to replace it.
- Resource Requests and Limits: Pods can specify their requests of CPU and memory needed, Kubernetes ensure they are scheduled on nodes that can share enough resources to meet these demands.
![[Pasted image 20250404130302.png]]
# MultiCloud Kubernetes Architecture

## Key Characteristcs of a Multi-Cloud Kubernets Architecture
Now that we have an overview of the internal architecture of the cluster it is possible to look for the important characteristics for a Multi-Cloud Kubernetes Architecture.
- Hybrid Deployment 
	- In a hybrid deployment is possible to run Kubernetes cluster both on premises data centers and in multiple public or private cloud environments. This approach makes the set-up more scalable and flexible.
	- Kubernetes facilitates hybrid deployments seamlessly across different environments. 
- Cross-Cloud Management 
	- Refers to the ability to manage Multiple kubernetes cluster running them as a single unified entity. There are many to obtain this resule, such as **Kubernetes Federations** or **Multi-Cloud Management Platforms**. 
- Cloud-Agnostic Design
	- A cloud-agnostic design means that the kubernetes environment is not tied to any specific cloud provider or platform. The entire infrastructure is designed to run seamlessly across multiple clusters and clouds without needing extra actions for each provider. Cloud agnostic solutions relies on the standard Kubernetes APIs and open-source tools to avoid vendor specific lock-in. 
## Benefits of Adopting Multi-Cloud Kubernetes [TO BE COMPLETED]


## Key Componets and Charateristics
### Connectivity
In a Multi-Cloud environment a robust and secure networking and connectivity mechanism is necessary to allowd different cloud providers to communicate effectively
Of course different tools can offer proprietary solution to connect pod-to-pod in a multi cluster environment.

There are many ways to make the cluster communicate:
#### Cross-cloud Communication with VPC and VPN
In Cross cloud communications we create reliable, secure communications channels between different cloud environments. And among the other two main techniques arise:
##### VPC Peering
 With **Virtual Private Cloud** peering is possible to obtain a private communication between networks (VPCs) in different clouds.
 The traffic does not go out in the public internet and also ensure low latency and high security.
 ##### VPNs 
 VPNs or **Virtual Private Networks** are encrypted tunnels for secure communication between different networks. It is mostly used for securely connecting clouds resources when in a separate providers. It is more general purpouse and is based on the outside internet to work
 
#### Service Meshes
A service mesh is a dedicated infrastructure layer that manages communication between microservices, especially in multi-cloud architecture. Abstracts the complexity of managing inter-service communications by providing feature such as traffic routing, load balancing, service discovery and security policies. 
The key aspects of **Service Meshes** are:
- Traffic Management
- Security
- Observability

Some popular service mesh solutions include [[Istio]], [[Linkerd]].

### Workload Distribution and Load Balancing

#### Workload Distribution

Workload distribution refers to the strategic allocation of tasks and responsibilities among clusters and nodes. Usually is possible to decide a policy that will be followed to distribute the workload.
Some multicluster solutions like [[Karmada]], [[KubeStellar]], [[Liqo]], [[Apache Yunikorn]], [[Open Cluster Management]], supply the user with CRDs that can be managed to decide the best allocation.

#### Load Balancing
Load Balancing is a technique used to distribute network traffic across a pool of servers known as *Server Farm*. The goal is to optimize networks performance, reliability and capacity by reducing latency as the demand is equally distributed among multiple servers and compute resources.
Included capacity of load balancer is **failover**, meaning that if a server fails a loadbalancer immediately redirects workloads to backup servers mitigating the effect on end users.
Usually load balancing is categorized as supporting either Layer 4 and Layer 7 of the OSI communication model.

Layer 4 load balencers distribute traffic based on transport data such as the IP addresses and TCP ports.
While Layer 7 load-balancing devices make routing decision based upon the application-level characteristics. 
#### How Load Balancing Works
Load Balancers handle incoming requests from information and other services. They are located between the servers and the internet.



```mermaid
flowchart LR
User --> Internet --> LoadBalancing --> Server --> Database
```

#### Multi-Cluster Orchestration Tools
Tools such as [[Rancher]] enables organizations to define policies for distributing workloads across different clouds, providing a centralized control plane for workload managements.

### Cluster Federation [TO BE COMPLETED]
