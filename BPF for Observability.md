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