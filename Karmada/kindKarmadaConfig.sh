# Host Creation
karmada/hack/create-cluster.sh host $HOME/.kube/host.config

# Installing Karmada on the host
kubectl karmada init --crds https://github.com/karmada-io/karmada/releases/download/v1.2.0/crds.tar.gz --kubeconfig=$HOME/.kube/host.config
