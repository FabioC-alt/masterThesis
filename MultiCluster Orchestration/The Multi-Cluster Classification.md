# Operators Multi-Cluster 
This is the common Multi-Cluster operators.
Here we can evidence the custom controller, the custom Kind and eventually a Custom-Subresource.

Tools like [[Karmada]] uses CRDs like the `PropagationPolicy` to declare the wanted state and then uses the `Controllers` to  obtain the wanted state throught actions. This is the common `Operator` pattern. 

Other tools that do the same [[Liqo]], [[KubeStellar]], [[Plural]], [[Rancher Fleet]].
# Git-Ops Multi-Cluster
This is the case of [[Rancher Fleet]].
Here there is no defined CRDs INSIDE the cluster to declare the wanted status, but instead a Git configuration stored somewhere from which we can derive the wanted state.

# Dashboard Multi-Cluster 
In this context there is no 