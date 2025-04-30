
# End-to-End User Request Flow
**Request routing**: *Dynamic DNS mapping* -> 

![[Pasted image 20250430115242.png]]

## Flow
User sends the request to the **facebook.com**, the DNS Server returns an IP address that is mapped to a Meta-operated small edge datacenter, this datacenter is called **PoP**(Point of Preference).

This dynamic mapping ensures that the choosen PoP is close to the user, while balancing load across PoPs. The user TCP connection is terminated at the PoP, which maintains separate, long-lived TCP connections with Meta's datacenters. The split-TCP set-up offers some advantages:
- Reduced TCP-establishment latency 
- Static-content Cashing
Reduced 

## PoPs 






