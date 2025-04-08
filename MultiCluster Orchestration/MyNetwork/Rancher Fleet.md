![[Pasted image 20250408112551.png]]

Allowds to manage using githubs repos up to one million clusters.

Rancher Fleet is a Cluster Engine container management tool to deploy engine designed to offer more control on the local cluster and constant monitoring through GitOps.

## Central Control Plane
The Central Control plane runs on a **Manager Cluster**. -> Is possible to decide which will be the manager cluster by installind the CRDs on it using helm.

The control plane is able to manage all the other clusters using the **namespace cluster**, where all the resources are deployed to be managed by the other remote clusters.
The agent in the managed clusters will be managed by the acces of a *token*.

## Agent on Managed Clusters
The fleet agent is installed inside the cluster that needs to be managed. It is possible to decide how to manage the clusters using a **configuration.yaml** file that will be launched along the helm command to install the agent with the creation of a new namespace.
Once the installation is completed in the namespace a fleet-agent will be running.
This command can be repeated as many time as clusters we have.

## Workload Management
To choose the cluster where to deploy certain resources we can create a `ClusterGroup`. 

## GitOps Integration in Local Cluster
First we need to be inside the control plane cluster and to create a `GitRepo` resource, from here is possible to decide which is the correct repo, which branch to use and which are the kustomization.
It is possible to decide the configuration using the helm installation.
All the application in the end will be helm charts, while Argo or Flux instead creates Kubernetes Manifests.

## GitOps Integration in Remote Clusters
The changes is done using the `target` key in the `GitRepo` resource.

## Drift detection and Reconciliation
Fleet does not detect the drift (2022). Is it still so?

# MultiCluster Detections



