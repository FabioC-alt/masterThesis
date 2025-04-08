# Kubernetes Operator Pattern
The kubernetes Operator is capable of understanding the needs for an application.
![[Pasted image 20250408123402.png]]

The Operator is based upon three main pillars

![[Pasted image 20250408123437.png]]
## Custom Resource Definition
The CRDs extends the Kubernetes API. The CRDs define the desired state, behaviour and the parameters for an application. Making it easier to manage complex applications in a Kubernetes-native way.

## Controller
The controller is in charge of monitoring and reconciling the state of the CRDs within the Kubernetes Cluster.
It primarly watches for changes in the CRDs and take the appropriate actions to ensure that the desired state, as defined in the CRDs is maintained.

## Operator Logic
The operator logic is a set of automated procedures, workflows and decision-making processes that operates to ensure that the applications aligns with its desired state as defined in the CRDs.

# What is it?
The Kubernetes Operator is a powerful pattern to manage applications. It extends the Kubernetes Capabilities by capturing domain-specific knowledge and operational procedures into custom resources which can be managed by Kubernetes itself.
![[Pasted image 20250408124224.png]]

## What were the fundamentals?
The operators where conceived and developed by the **CoreOS**.
CoreOS introduced the concept of operators to the Kubernetes Community as an open-source project.

## Workflow in operator managed systems
The systems wheter they are internal or external triggers changes in an Operator by sending events or requests that pertain to the application or workload managed by the operators. Once an operator receives the trigger it interacts with the Kubernetes API server to create and update the CRDs.

![[Pasted image 20250408125054.png]]

State Reconciliation flow: 
![[Pasted image 20250408125420.png]]

# Patterns

## Custom Kind + Custom Controller
The main `Operator` pattern can be represented as `Custom Kind + Custom Controller`.  This is the most popular pattern. In this pattern there are some Kind to a declarative model in the domain requirement. Also the pattern incorporate a custom controller that includes the logic to reconcile the state by reacting to the events.
This pattern can be implemented with the use of the CRDs and AA(Api Aggregation) mechanism.
## Custom Kind + Custom Controller + Custom Sub-resource
This is a variation on the `Operator Pattern`. It also supports custom actions (beyond the CRUD) on the custom Kinds. This pattern is implemented only using the AA mechanism.

## Custom Controller + Custom Sub-resource
In this pattern there is no new Kind defined. The custom controller executes its reconciliation based on the events related to the Kinds already registered in the cluster. 
The job of the custom sub-resource is used to retrieve information that is collected by the custom controller.
This pattern can be implemented only using the AA mechanism.


![[Pasted image 20250408155235.png]]



https://itnext.io/comparing-kubernetes-api-extension-mechanisms-of-custom-resource-definition-and-aggregated-api-64f4ca6d0966

https://medium.com/tech-at-fidelity/kubernetes-operators-pioneering-modern-architectural-automation-and-management-5bf2fba11d35