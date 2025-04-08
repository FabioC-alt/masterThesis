****
Plural is a unified cloud orchestrator for kubernetes managements at scale. 

Plural decompose the fleet management in 4 main concerns:
- Kubernetes Continuous Deployment -> by exploiting GitOps-based mechanism is possible to sync kubernetes yaml, manifests.
- Kubernetes Dashboarding -> Using SSO-integrated Kubernetes dashboard layer for ad-hoc infrastructure troubleshooting.
- Infrastructure-As-Code 
- Self-Service Code Generation

# Architecture
Plural is based upon a scalable, secure, agent-based pull architecture. 
There is no need for direct access to any of the clusters it deploys to. It can manage workloads in any cloud, on-prem, on the edge or with KIND.

Does not require a Kuberentes network intensive stream, nor central access to a kubernetes cluster, and it does not rely on a single-mastered operator control loops.

Thanks to the **auth proxy** is also possible 