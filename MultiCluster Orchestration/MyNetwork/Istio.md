
Istio is a service mesh infrastructure layer that gives application capabilities like zero-trust security, observability and advanced traffic management without code changes. It enables mTLS encryption, policy management and access control.

Istio allows multi-cloud, hybrid and on-prem with a single mesh.

In istio the multicluster-management is splitted using multiple control-plan, each for a different cluster.

To manage the complexity of a service mesh is possible to use Admiral CRDs

## Sidecar vs Ambient Mode in Istio
Ambient mode in Istio was introduced to overcome the shortcomings of the Sidecar mode. It is based on a two level architecture.

At base level is possible to find the **ztunnel**, also called Zero Trust Tunnel, it is component that aims to power's Istio's ambient data plane mode.
The Ztunnel is responsible for securely connecting and authenticating workloads within the mesh. 

The second layer of the ambient mode is the **Waypoint Proxy** which is a deployment of the [[Envoy]] proxy. The Waypoint Proxy runs outside of the application pod and are completely independent from the application

It is possible to use only the ztunnel if not interested in Authorization, telemetry and Virtual Service Routing
