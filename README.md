# Kafka Kubernetes cluster
### Pre Requirements
- Container runtime (Docker)
- Kubernetes cluster with 3 nodes. One Master and two worker

## Setup Kubernetes cluster
You can follow Kubernetes [official documentation](https://kubernetes.io/docs/setup/) to bootstrap clusters with kubeadm.
### Nodes
```
~ kubectl get nodes
NAME           STATUS   ROLES                  AGE     VERSION
k8s-master01   Ready    control-plane,master   14m     v1.21.0
k8s-worker01   Ready    <none>                 3m10s   v1.21.0
k8s-worker02   Ready    <none>                 2m36s   v1.21.0
```

## Kafka cluster
After cloning the repository create all manifests:
```
~ kubectl apply -f kafka_sample/Manifests/
```
#### Pods
```
~ kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
consumer-replicaset-f86784c7b-9b24n   1/1     Running   0          114s
consumer-replicaset-f86784c7b-bsfjt   1/1     Running   0          114s
kafka-deployment-75bb9865b-44v2z      1/1     Running   0          113s
kafka-deployment-75bb9865b-wwjsx      1/1     Running   0          113s
producer-pod                          1/1     Running   0          113s
producer-replicaset-c825f             1/1     Running   0          113s

```
#### Topics
As it has been mentioned in [Producer](https://github.com/divergentluna/kafka_sample/tree/master/Producer) and [Consumer](https://github.com/divergentluna/kafka_sample/tree/master/Consumer) part  there are two kafka topics: 'input' and 'output'

## Monitoring
Using [kube-promethus](https://github.com/parsa97/kube-prometheus) github repository to create Prometheus, Grafana and Alertmanager dashbords.
You can follow the instructions from [Here](https://github.com/parsa97/kube-prometheus/blob/main/README.md).
#### Access Dashboards
##### Prometheus
```
~ kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090
```
##### Grafana
```
~ kubectl --namespace monitoring port-forward svc/grafana 3000
```
##### Alertmanager
```
~ kubectl --namespace monitoring port-forward svc/alertmanager-main 9093
```

