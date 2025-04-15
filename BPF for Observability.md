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