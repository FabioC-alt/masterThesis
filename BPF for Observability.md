```
#include <linux/bph.h>
#define SEC(NAME) __attribute__((section(NAME, used))

SEC("tracepoint/syscall/sys_enter_execve")
int bpf_prog(void *ctx){

	char msg[] = "Hello, bpf world!";
	bpf_trace_printk(msg, sizeof(msg));
	return 0;

}

char _license[] SEC("license") = "GPL";
```
Thanks to the attribute `SEC(NAME)`, the program will be run only when the tracepoint detects an execve sys call


# eBPF
![[Pasted image 20250415121437.png]]https://ebpf.io/what-is-ebpf/#what-is-ebpfio

![[Pasted image 20250415122600.png]]

![[Pasted image 20250415122611.png]]

Cluster Mesh CIlium:
https://www.youtube.com/watch?v=VBOONHW65NU&ab_channel=eBPF%26CiliumCommunity

eBPF observability in Cilium:
https://www.youtube.com/watch?source_ve_path=Mjg2NjQsMTY0NTAz&v=8WCbGSCyDSo&feature=youtu.be

ViperProbe -> Observability in Microservices with eBPF:
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9335808


eBPF: A New Approach to Cloud-Native Observability, Networking and Security for Current (5G) and Future Mobile Networks (6G and Beyond):
https://ieeexplore.ieee.org/abstract/document/10138542


Observatory: Fast and Scalable Systems Observability:
https://cs.brown.edu/media/filer_public/81/8d/818d0534-f99f-4089-820a-5a7b9b52ff07/yalavartiarvind.pdf