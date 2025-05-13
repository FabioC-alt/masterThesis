EVALUATING AND MODELING VIRTUALIZATION
PERFORMANCE OVERHEAD FOR CLOUD ENVIRONMENTS:
https://www.scitepress.org/Papers/2011/33889/33889.pdf

Effects of communication latency, overhead, and bandwidth in a cluster architecture
https://dl.acm.org/doi/abs/10.1145/384286.264146

Managing Performance Overhead of Virtual Machines in Cloud Computing: A Survey, State of the Art, and Future Directions
https://ieeexplore.ieee.org/abstract/document/6670704?casa_token=FFDLhut_HM8AAAAA:9n70cdPzDSfnyMy2dfHMK4vdL1XVS1lqOjmxzf8n-n2cysTT9CICxkZe8cTVKLqyTxMA1TO5

## Causes and metrics of VM performance overhead in IaaS cloud



The Good, the Bad and the Ugly of Consumer Cloud Storage
https://dl.acm.org/doi/pdf/10.1145/1842733.1842751?casa_token=TFOIbDyNexcAAAAA:9a-GP4VGcKja3nlt0mmeC0q1UIB8mOJGvn5SUwhtpshQrXeR1eFvpxqtGBJwt0XRZy6kt5GnJJJa

Profiling and Understanding Virtualization Overhead in Cloud
https://ieeexplore.ieee.org/abstract/document/7349558?casa_token=5To0uuCWdbkAAAAA:-COBv94a8UPLVcvhp8zelG3Jo4vAPrDuM0cIhHKTctLOI_50Qq-


Liqo
https://medium.com/the-liqo-blog/benchmarking-liqo-kubernetes-multi-cluster-performance-d77942d7f67c

https://arxiv.org/abs/2204.05710

# Test Analysis
https://medium.com/the-liqo-blog/benchmarking-liqo-kubernetes-multi-cluster-performance-d77942d7f67c


# Overhead definition


## Experiments
Performance Overheah:
a) Experiments is executed to quantify the performance overhead of the virtualization problem
b) Number of VMs and other resources management-related factors is investigated in two different scenarios, focused on *scalability* and *over-commitment*.

For scalability one increased number of VMs until all available physical resources are used. 

## Testbed
The testbed was made with two Kuberntes cluster: one is the *resource provider*, the other is the *resource consumer*.


# Performance Metrics of Local Cloud Computing Architectures
https://ieeexplore.ieee.org/abstract/document/7371454

****

Encyclopedia of Computer science
https://dl.acm.org/doi/pdf/10.5555/1074100.1074668

*Overhead* in computer systems is like overhead in organizations- shared functions that benefit everyone but which cannot be allocated conveniently to one activity. 

In computer systems, allocation of resources, scheduling, conflict resolution, protection, security, performance monitoring, auditing, accounting, I/O control, caching, distributed functions and network protocols are all counted as overhead.

Overhead in computer systems shows up as slower process, less memory, less network bandwidth or bigger latencies than would be expected from reading the system specifications.

Overhead is not easy to measure. The time an operating systems spends in supervisor state is not pure overhead because many important operations requested by user tasks are implemented as system functions that run in supervisor state.

The following are all counted as overhead:
- *Allocation of resources*
- *Error Correction*
- *Exceptional Conditions*
- *Protection and Security*
- *Performace Monitoring, auditing and accounting*
- *Input-output control*
- *Caching*
- *Distributed Functions*
- *Network Protocols*



Top 10 Kubernetes Metrics for Enhanced Visibility and Control
https://www.groundcover.com/kubernetes-monitoring/kubernetes-metrics?utm_source=chatgpt.com

## Kubernetes Metrics



## My Monitoring

Testbed:
3 cluster w/ 3 node per each -> 1 control plane, 2 worker
Default 

CPU Usage: 
Kubernetes Vanilla 
Karmada
Liqo