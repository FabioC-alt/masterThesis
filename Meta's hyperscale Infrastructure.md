
# End-to-End User Request Flow
**Request routing**: *Dynamic DNS mapping* -> 

![[Pasted image 20250430115242.png]]

## Flow
User sends the request to the **facebook.com**, the DNS Server returns an IP address that is mapped to a Meta-operated small edge datacenter, this datacenter is called **PoP**(Point of Preference).

This dynamic mapping ensures that the choosen PoP is close to the user, while balancing load across PoPs. The user TCP connection is terminated at the PoP, which maintains separate, long-lived TCP connections with Meta's datacenters. The split-TCP set-up offers some advantages like Reduced TCP-establishment latency 
## PoPs 
PoPs are datacenters composed by hundreds of servers. The PoPs are positionated worldwide to ensure that most users have a PoPs close to them and thereby ensuring short network latencies.

PoPs are also useful for storing media contents such as video, images and music. Also it is possible to store these type of content inside CDNs. 
A CDN site typically has tens of a hundreds of servers.

## PoPs-to-datacenter 
Traffic travels through Meta's private wide-area network, which globally inter-connects Meta's PoPs and datacenters  using optical fibers spanning tens of thousand of miles. 
This WAN provides high bandwidth to serve this internal traffic.
## Infrastructure Topology
![[Pasted image 20250430121256.png]]

Gloabally there are around 10 regions datacenters. Each of these has multiple datacenters located within the radius of a few miles. 








