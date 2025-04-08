FlatCar is a minimal linux container image optimized for cloud-deployment. The Os is shipped with an immutable filesystem and includes automatic atomic updates.

## Pros
Only-read immutable os, with atomic changes, so there is no possibility to manomission. Also only at reboot the updates are lauched, this is done to avoid down time.
Docker and Containerd are preinstalled.
Low-usage optimal for edge and embedded systems. 
FlatCar was created with a centralized approach in mind. -> Ignition

## Concepts

FlatCar is powered at *provisioning time*, and there are two main configuration lenguages to power up FlatCar. 
### Butane 
Butane is a human-readable/writable YAML