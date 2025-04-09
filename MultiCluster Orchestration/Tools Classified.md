#### **1. Karmada**

- **Pattern**: Custom Kind + Custom Controller
    
- **How**: Uses CRDs like `Policy`, `Cluster`, and `Work` with custom controllers for resource propagation and scheduling across clusters.
    
- **Extra**: Uses AA to extend Kubernetes API.
    

#### **2. KubeStellar**

- **Pattern**: Custom Kind + Custom Controller + Custom Sub-resource
    
- **How**: Defines custom Kinds for placement and synchronization, and includes sub-resources for extra control and observability across clusters.
    

#### **3. Liqo**

- **Pattern**: Custom Kind + Custom Controller
    
- **How**: Extends the API with virtual kubelet-backed resources using CRDs like `Peering`, `Advertisement`, and more. Controllers handle auto-discovery and federation logic.
    

#### **4. Rancher**

- **Pattern**: Custom Kind + Custom Controller
    
- **How**: Uses multiple CRDs (e.g., `Cluster`, `Project`, `App`) with controllers for lifecycle and access management.
    
- **Extra**: Heavy use of AA and API extension.
    

#### **5. Rancher Fleet**

- **Pattern**: Custom Kind + Custom Controller + Custom Sub-resource
    
- **How**: Manages GitOps deployments using CRDs like `Bundle`, `ClusterGroup`, and `Fleet`, with status sub-resources.
    

#### **6. Istio**

- **Pattern**: Custom Kind + Custom Controller
    
- **How**: Implements custom Kinds like `VirtualService`, `DestinationRule`, etc. Uses a control plane (Istiod) with controllers to manage behavior.
    

#### **7. Linkerd**

- **Pattern**: Mostly Controller + Sub-resource (uses existing Kinds)
    
- **How**: Annotates existing Services/Deployments and reconciles them using controllers. Has dashboards and APIs to expose status.
    

#### **8. Apache YuniKorn**

- **Pattern**: Custom Controller + Custom Sub-resource
    
- **How**: Schedules workloads using custom logic without introducing many new Kinds, but has AA-based metrics and data access.
    

#### **9. Open Cluster Management (ACM)**

- **Pattern**: Custom Kind + Custom Controller + Sub-resource
    
- **How**: Defines Kinds like `Placement`, `ManifestWork`, `ManagedCluster`. Controllers manage lifecycle, placement, and health reporting.
    

#### **10. MultiCluster Orchestration (General Category)**

- Often uses **Custom Kind + Controller** to define scheduling and placement rules across clusters, especially for GitOps and federation tools.
    

#### **11. Plural**

- **Pattern**: Custom Kind + Custom Controller
    
- **How**: Uses CRDs and controller logic to automate the deployment and management of applications in Kubernetes.
    

#### **12. FlatCar / Container Runtime / Confronto alla Messicana**

- **Not directly using the patterns** (OS/runtime level), but these may be:
    
    - **Subjects of management** using those patterns.
        
    - **Inputs to CRDs** for e.g., node-specific configurations.
        

---