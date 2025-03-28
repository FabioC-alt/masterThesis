# [[Karmada]]

In karmada to schedule the workload we can use either the PropagationPolicy or the ClusterPropagationPolicy where the first is the is the namespace-scoped resource type and the cluster is the cluster-scoped resource type. Using this two resources is possible to schedule the workload either in one namespace or in one cluster

# [[Liqo]]
In Liqo there are two different mechanism to schedule the workload:

- First: Admins can enable offloading and choose where to put a specific namespace and selecting a specific subset of remote clusters for the execution of the workload → this it done by scheduling some workload to a virtual node
- Second: Is possible to restrict the elegible targets for each workload based on the requirements
# [[Open Cluster Management]]
In OCM is possible to decide where a certain workload should fit using the Placement resource, and it is used to dynamically select a set of managed clusters in on or multiple managed cluster set thus making possible a multi-cluster scheduling.