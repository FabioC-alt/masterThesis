Toward a high availability cloud: Techniques and challenges
https://ieeexplore.ieee.org/abstract/document/6264687?casa_token=R0ZiiW_kZz8AAAAA:Bf86ydrh6eb4N_xTu0PvOOEQOjrNCoSF4IIS_rY42rk43IVZZRbryAxwnmS4y1hqAjcG47fT


High-availability clusters: A taxonomy, survey, and future directions
https://www.sciencedirect.com/science/article/pii/S0164121221002806?casa_token=Jp6iCx9MkUUAAAAA:q50XpNekaUFOUsc4SDz6atxHKke7LLSAWfLZ0iT49olGQJRZSFjPxpSK4w9mZOsv2_H4dD9udg
# High Availability in Cloud
## Key Concepts and Terminology
The ISO/IEC 25010 standard defines as the "*degree to which a system, product or component is operational and accessible when required for use*".

Availability is calculated as the ratio between the time over which the system was observed. Equivalently, availability can be computed as the ratio between the *mean time between failures*, MTBF and the sum of the mean time between failures and the mean time to recover after failures.


# Availability in the cloud: State of the art
https://www.sciencedirect.com/science/article/pii/S1084804515002878?casa_token=Db-Jp6fhqzgAAAAA:nzSrg1IYg0EtvI6SCmbf9crpP7_3w-iGxNSUiqj4tU-Wr2yYARsi4ltqwq21lLBkf6-o1SHhCQ

Availability is a non-functional requirement specified in terms of the percentage of a system or a service is accessible. This percentage determines the allowed outage time for a given period.
High Availability(HA) is a strict requirement and refers to an availability of at least 99.999% of the time, which is approximately 5mins every year.

 However each cloud provider defines availability from
its own technological perspective and provides architectural
solutions and services based on specific definitions. These different
definitions use similar terms but with different interpretations and
measures.
Furthermore, many research papers relate availability to other characteristics of the cloud, such as performance, scalability, elasticity and security; they do not
propose a comprehensive solution that would guarantee availability in the cloud.

This paper surveys current availability solutions in cloud pro-
viders' practices, and those proposed in research papers from the
academia and the industry. For this purpose, we first define a
taxonomy inspired by the Service Availability Forum (SA Forum)
(Toeroe and Tam, 2012) concepts and mechanisms to set the
baseline for the evaluation. 

The TL 9000 Quality Management System
from the QuEST Forum (QuEST Forum, 2010) for the information
and communication industry defines availability as “The prob-
ability that the system is operational when required” and it is
calculated by system uptime over the total time required to be
operational.

![[Pasted image 20250509162900.png]]
One can view the availability of a system through the avail-
ability of its services. Service availability can be defined as:
![[Pasted image 20250509163028.png]]


We talk about HA if a system or a service is available at least
99.999% (a.k.a. five nines) of the time, which allows for a max-
imum of five minutes and 15seconds downtime per year 

Cloud providers consider availability within the context of a
Service Level Agreement (SLA).

![[Pasted image 20250509163555.png]]

