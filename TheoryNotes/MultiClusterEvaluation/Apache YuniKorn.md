[[Apache YuniKorn]] is a light-weight, universal resource scheduler for container orchestration systems. 

The particularity of the Apache Yunikorn [[Workload Scheduling]] is that it is app-aware. The default k8s scheduler simply schedules pod by pod without any context about user, app or queue. However YuniKorn recognize users, apps and queue. It considers more factors when performing Scheduling decisions.

## [[Gangs]]
Apache YuniKorn uses the concept of Gang to schedule a set of resource all at once. Ideally, the gang defines all the resources the application needs to start. It is possible to create multiple gangs of different specifications for one application. 

## [[Working Queues]]
Applications can be queued in working-queues. Using the `OrderingPolicy` is possible to determining which applications can get resources first.

## Architecture

![[Pasted image 20250401151138.png]]

### Core Scheduler
The core scheduler encapsulates all scheduling algorithms, it collects resources from underneath resource management platforms. Responsible of container allocation requests.
The job is to make the decision about where is the best spot for each request and then sends response allocation to all the resource management platform.
### Scheduler Interface
The Interface defines the protobuf interface for the communications between the yunikorn-core and the management systems.

### Kubernetes Shim
Responsible for talking to Kubernetes, responsible for translating the Kubernetes cluster resources and also sends resource requests via scheduler interface and send them to the scheduler core.
#### Design of the Kubernetes Shim
When a scheduler decision is made, it is in charge of binding the pod to the specific node.
The Kubernetes shim is based on the Application Controller.

**Admission Controller**
The kubernetes shim is separate pod that runs two `webhooks`:
- `MutationWebhook`: Which is in charge of modifying incoming pod specifications before they are scheduled.
- `ValidationWebhook`: Ensures configurations correctness before applying changes to Kubernets

The Admission Controller can be scheduled via the YuniKorn **Helm Chart**, and loads the kubernetes secrets containing the CA certificates. It generates and rotate TLS certificates. Also runs the HTTPS server for webhook interactions.







TEST

