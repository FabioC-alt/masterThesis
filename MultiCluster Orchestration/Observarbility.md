# The OTel Project
The OTel project is relevant for the telecom domain for several reasons. 
It is an horizontally-aligned telemetry framework across the three observability pillars and the goal is to keep a vendor neutral objective.
It is the result of the join between OpenTracing and OpenCensus and it is driven by CNCF.
![[Pasted image 20250414174137.png]]

## The key aspects

- **Horizontal with respect to the API and SDK choosen**
- **Common Data Models and Semantic Conventions**
- **Efficient Ways to collect, process and forward the data**

The OTel project is relevant to the telecom community domain for many reasons:
- Stateless Agent Deployment Model
- Pick/Choose/Design an OTel Collector
- End-to-end metric data push will result in latency reduction 
- Data Alignment results in mean time to resolve

# MultiTenancy and Observability in Smart City Platforms

The observability is the property that measures how well internal states of a system can be determined from knowledge of its external outputs.
A system is considered to be observable if the current state can be estimated using only the informations available by the outputs.
Usually in mechanical engineering this is archieved using sensors.
In ICTs the data are gathered by measuring variuous properties of the system and it is the only source of information available to estimate the system's internal state.

## Smart Cities Platform Requirements


#### Scalability to grow together with the Smart City's need
It is impossible to find a one-fits-all measure for the smart cities need, so the infrastructure needs to be tailored for the city studied, and also as the city grows and its shape changes it is necessary to further adapt the model to the growing process of the monitored entity.
#### Flexibility to integrate with different systems, services and data sources
The system's employed to monitor the city cannot use just one standard as the city is an heterogeneous entity and so multiple techonologies, services and data sources must be used to monitor and observe the data coming from it.
#### Openess to expose data to third parties
In order for the investments made by the commitee to be capitalized and be useful for the community the data must be available to be shared among the community, in order to be used for further applications.
#### Compliance with local, national, international regulations for data privacy and security
Due to the sensibility of the data involved in the Smart City the information gathered by the system's must be strictly encrypted and collected according to the national or sovra-national regulations.
#### Availability
In order for the data to be useful the monitoring should be performed 24/24 7/7 and 365/365.
#### Reduction of the Smart City environmental footprint
The Smart Cities must be sustainable in order to contribute toward a more sustainable use of the city's resource.

## Smart Cities Platform Stake Holder
The main stakeholder in the operations for the SC Platforms are:
- Infrastructure Operations: Mainly the support operations
- IoT Sensors Operations: Data retreiving
- Business Operations: Defining the KPI for the services offered and archived

## Observability of Smart City platforms
The complexity of a SC Platform in terms of technology, requirements, and stakeholders involved make observ-
ability an important aspect that needs to be taken into account in the software architecture design parameters
of the system.


![[Pasted image 20250502111115.png]]
