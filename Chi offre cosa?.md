Prima classificazione?
Quali sono le feature di ogni tool?

## Karmada

![[Pasted image 20250516092626.png]]

Questo può essere implementato come hub-spoke oppure master-slave. 

### Multi-policy multi-cluster scheduling
Karmda is capable of supporting multiple scheduling strategies.

### Cross-cluster failover of applications
Karmada automatically migrates faulty cluster replicas in a centralized or decentralized after a cluster failure.

### Cross-cluster service governance

Done using submariner:
Submariner allows two or more cluster, with a high level of trust, to communicate and share services amongst themselves. Within a cluster set, all namespaces with a given name are considered to be the same cluster.

To connect the clusters, it uses Submariner

Cross-cluster Service Governance is performed using `ErieCanal`.

### Karmada Workload 
Karmada handles multi-cluster resource scheduling -> unique feature

PropagationPolicy and ClusterPropagationPolicy APIs are provided to propagate resources.


## Liqo
Usa per la connessione fabric -> Wireguard: VPN


## Admiralty
https://admiralty.io/docs/concepts/topologies
Supporto per topologie: **Decentralized Federation**
Progetto un poco inattivo per il resto


### 

























