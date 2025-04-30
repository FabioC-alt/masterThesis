### Intro
Service mesh creates a mesh of proxy (usually Envoy). 
The Control plane and data plane are still present and works for the aims of connecting the pods.

The benefits of the service mesh are:
- Connect
- Secure data flow
- Control The traffic 
- Observing the traffic
Drawbacks:
- Capacity and Resources -> cause the service mesh use resources
- Network Latency -> Proxies uses networking and can create latency
- Sometimes is not removable 
- Auxiliary Infrastructures


Service Mesh are used mostly for mTLS. 
A quanto pare non esistono alternative per service mesh


**sidecar mode**, which deploys an Envoy proxy along with each pod that you start in your cluster, or running alongside services running on VMs.
**ambient mode**, which uses a per-node Layer 4 proxy, and optionally a per-namespace Envoy proxy for Layer 7 features.
https://imesh.ai/blog/istio-ambient-mesh-vs-sidecar/

# Service mesh 

![[Pasted image 20250430170749.png]]

Traditional Service meshes are based upon *sidecars*. Each service instance (or pod) has a dedicated sidecar proxy that manages service-to-service communications, security and observability.

## Drawbacks
High memory and CPU utilization
Fixed Operational Cost
Service Disruption


# Ambient Mesh
- **ambient mode**, which uses a per-node Layer 4 proxy, and optionally a per-namespace Envoy proxy for Layer 7 features.

Ambient Mesh — An Evolution of the Service Mesh:
https://medium.com/@rajneeshkaggarwal/ambient-mesh-an-evolution-of-the-service-mesh-af768e397a29

Spilts the **data plane** configuration into two layers:
- L4 -> ztunnel
- L7 -> handled by the Waypoint Proxy

![[Pasted image 20250430171632.png]]

zTunnel is the **node-level component**, which means the for each node a zTunnel is deployed.
The zTunnel is responsible for automatic mTLS, TCP-level routing.

The Waypoint proxy is the **namespace-level envoy instance**. It is responsible for **HTTP rounting**, **Authorization Policies**, **Telemetry** and **Traffic Shaping**.

