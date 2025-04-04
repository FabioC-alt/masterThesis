# Che tipo di architettura usano?

 [[Liqo]] usa una struttura peer-to-peer il che significa che su ogni cluster abbiamo un virtual node deployed che è quello su cui scheduliamo il workload per l'offloading, ma volendo posso anche schedulare sul secondo nodo un nodo virtuale che rimanda al primo.
 
[[Karmada]] a suo modo usa una struttura master-slave perchè abbiamo un control plane che controlla i cluster, cluster che sono registrati tramite il Karmada Controller.

[[Open Cluster Management]] è una soluzione basata su un sistema Hub-agent. Difatti qui abbiamo una struttura master-slave perchè c'è un control plane hostato su un cluster detto **Hub** che controlla una serie di cluster per mezzo di un agent. 

[[KubeStellar]] è una soluzione interessante, nonostante non sia strettamente master-slave, ne ricorda il funzionamento, perchè ci sono una serie di cluster connessi tramite OCM, che sono gestiti tramite un sistema Hub-spoke. Quindi diciamo che un control plane che fa questo lavoro ci deve essere. 
Ma nonostante ciò, usa il concetto di spaces. Gli spaces sono entità più astratte.

[[Apache Yunikorn]] è principalmente usata per schedulare risorse sui vari clusters. Comunque l'architettura non è chiaro se sia master-slave ma il principio sembra quello. Perchè il control plane sembra contenere principalmente il **Core** e lo **Scheduler**, mentre l'equivalente dell'agent sembra essere quello che viene chiamato li **Shim**.

## Vantaggi e Svantaggi

https://www.plural.sh/blog/kubernetes-multi-cluster-guide/?utm_source=chatgpt.com
https://medium.com/%40cpsupriya31/understanding-master-slave-architecture-uses-and-challenges-2acc907de7c4
![[Pasted image 20250404161517.png]]
The master-slave architecture is a design pattern in which one or more subordinate units known as slaves are controlled and coordinated by a central entity known as the master.

Problems with the Master-Slave Architecture
#### Single point of Failure
in many of the previously analyzed architectures and tools we are presented with the **Single Point of Failure** problem because as the central control point fails it is impossible to keep managing the system unless failover techniques are used as countermeasure. [Karmada]] propose a failover solution for cluster that are no more available and exploits the taints to avoid rescheduling thanks to the taintsmanager.
#### Communication Bottlenecks
Given that the master manages all tasks and gathers slave results, it may be prone to performance bottlenecks. If the workload or number of slaves get too great. The master may struggle to manage all the incoming requests.
#### Synchronization and Communication Overhead
Keeping synch and communications between the master and slaves can add complexity and overhead. Coordination methods are necessary along with data exchange protocols and network latency which can have influence on overall system performance.
#### Scalability Limitations
The design master-slave enables scalability by adding additionals slaves but there migh be restrictions due to the system's foundamentals constraints.