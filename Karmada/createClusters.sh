#!/bin/bash

# Ensure the .kube directory exists
mkdir -p $HOME/.kube

# Delete existing clusters if they exist
kind delete cluster --name=member1
kind delete cluster --name=member2

# Create the first Kind cluster
kind create cluster --name=member1 --config=cluster1.yaml
cp $HOME/.kube/config $HOME/config-member1  # Use cp instead of mv

# Create the second Kind cluster
kind create cluster --name=member2 --config=cluster2.yaml
cp $HOME/.kube/config $HOME/config-member2  # Use cp instead of mv

# Merge the kubeconfig files
# KUBECONFIG=$HOME/config-member1:$HOME/config-member2 kubectl config view --merge --flatten > $HOME/.kube/config

# Modify IP addresses (optional)
sed -i "s/127.0.0.1/172.30.2.2/g" $HOME/config-member1
sed -i "s/127.0.0.1/172.30.2.2/g" $HOME/config-member2

# Copy modified config files to remote machine
scp $HOME/config-member1 root@172.30.1.2:/root/.kube/config-member1
scp $HOME/config-member2 root@172.30.1.2:/root/.kube/config-member2

exit

