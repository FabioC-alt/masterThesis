# Hub-Spoke
[[Open Cluster Management]]
[[Karmada]] in Pull-mode

Nel modello Hub-Spoke non c'è una gerarchia stretta, vale a dire che il master non ha influenza diretta sugli slave. Sono gli slave che fanno delle richieste in maniera continuativa per essere aggiornati sullo stato che devono avere.

Pro: 
Il master non viene sommerso di richieste dagli spoke. Gli spoke sono indipendenti. Se il master crasha, gli spoke continuano a operare indipendentement.

Contro:
I cluster dipendenti sono occupati con la gestione delle richieste di pull per ricevere le direttive dal master -> mitigato dal fatto che se crashano, non è un problema
I cluster slave ricevono le direttive solo quando fanno polling al master, questo implica che le modifiche non sono subito effettive.


# Master-Slave
[[Rancher]]
[[Karmada]] in Push-mode

In questo caso la gerarchia è più stretta, è il master a mandare le direttive ai suoi sottoposti che le ricevono mediante un delegato che ha una connessione diretta con il master. 

Pro:
Il master ha una connessione diretta con i suoi sottoposti, quindi le direttive sono eseguite in maniera più rapida, ovvero quando il master decide che diventano effettive e vengono comunicate agli slave mediante l'agent.

Contro:
Questo approccio molto più a stretto contatto nel rapporto tra master e slave, rischia di rendere gli slave troppo dipendenti dal master.
Rancher ha sviluppato una procedura per il quale se un cluster agent smette di comunicare, uno dei node agent crea un tunnel per comunicare con il master e continuare a ricevere direttive.


# Consumer-Provider
[[Liqo]]

In questo caso non esiste gerarchia. Il consumer e il provider sono sullo stesso piano. L'utente può gestire le risorse come se fossero tutte nello stesso cluster.

Pro:
Si aumentano le capacità di computazione e gestione delle risorse. Aumenta la grandezza delle applicazioni deployabili sul "cluster".

Contro:
In questo sistema non c'è veramente un limite tra un cluster e un'altro, quindi se su un cluster è in esecuzione una applicazione e questo crasha, potrebbe portare con sé delle parti dell'applicazione importanti per il suo funzionamento.

# Connections 
## Tunnel Based
[[Submariner]]
In questa architettura il goal è di connettere molteplici cluster in maniera sicura. Viene definito un cluster set, ovvero un gruppo di cluster con alto grado di affidabilità che possono connettersi fra loro sfruttando la Public Network.

Pro:
Molto semplice da gestire nell'aggiungere i cluster nel cluster set. 

Contro:
Poco controllo sulle risorse che vogliamo includere.

## Service Mesh 
[[Istio]] 
Nell service mesh abbiamo un overlay network che incapsula i dati e li rende protetti. 

Pro:
Le service mesh di default possono essere usate per implementare la sicurezza e il monitoraggio.

Contro: 
Aumenta la complessità di gestione e di set-up.

Bonus: 
Le service mesh volendo potrebbero essere usate con un controller per avere una strategia di gestione di risorse in multi-cluster.

