## Replicated vs Split-by-Service
In a replicated setup is possible to have multiple copy of the application, *especially if the application is very light*.

In a Split-by-Service approach each part of the application is splitted into more services, deployed on different clusters.
It is also possible to choose wether to use a certain hardware for a particular cluster whether an other.

## Geographic Control and Data Sovereignty

For organizations operating in multiple regions or countries, multi-cluster Kubernetes offers precise geographic control over data. You can deploy clusters in specific locations to comply with data sovereignty regulations, ensuring data resides where it needs to be. This localized approach also improves application performance for users in different geographic areas by reducing latency. For instance, a healthcare provider might use separate clusters to store patient data in different countries, complying with local regulations.

## Edge Computing and IoT Enablement
In edge computing it is useful to put the data where they're needed, the users. In a decentralized approach we have latency reduction, bandwidth improvement in efficiency, and enables real-time processing for time-sensitive applications. 

# Benefits of Multi-Cluster Kubernetes
Multiple cluster can be managed separately so improving security and resource optimization.

# Multicluster Use case

## Geographically distribution
Having multiple clusters is necessary to have low-latency services in a geographically distributed system made of multiples clusters.
## Prod and Dev separation
Separating production and developement on multiple clusters avoids data leaks and makes possible to test new features.
## Cross-Cloud Strategy
Using multiple clouds to leverage and avoid vendor lock-in
## Multiple Cluster Configurations
It is possible using tools such as Terragrunt to keep infrastructure DRY and easy to maintain. 
## LoadBalancing
Having loadbalancer techniques allows the user to focus on other tasks instead of managing the traffic manually. Many solutions rised. Such as CloudFlare.

# Management models
## Kubernetes Centric
Specialized tools to treat all clusters as a unified system. This approach streamlines operations and centralized control, simplifying tasks like deployments and policy enforcement. 
This approach is effective when a constant configuration is needed among all the clusters.

## Network-Centric 
This model use a massively service meshes to establish secure and reliable communications between services running in different clusters. This approach give its best when applications components are distributed across multiple clusters and need to interact seamlessly. 

Service Meshes in this situations are critical because they allowds to create a dedicated infrastructure layer for managing inter-service communications while offering features like traffic management, security policies and observability. 

# Multi-Clusters Tools and Features

## Unified Control Plane 
In the architecture where we have one control plane that acts as conductor is possible to have a simplyfied managed cluster with the use of one single interface for all the clusters.
In this case context switching is not necessary and we have a reduced risk error.

## Opensource (well-known tools)
#### Karmada
#### Rancher Fleet
#### OCM

### Configurations Management Tools
Thanks to tolls like, FluxCD, ArgoCD and Projectsveltos is possible to use the same standards and simplyfies operations 

## Observability 
Vuoto -> non ci sono tools, Opentelemetry non sembra supportare il multicluster
-> Forse Observability con Istio
# Best Practice for a MultiCluster Kubernetes
The git approach -> using the git hub repo allows also to use the FluxCD and other continuous deployment tools.

