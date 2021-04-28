# Kafka Epoch Producer
This producer continuously write messages to 'input' topic with epoch timestamp in ms.
### Pre Requirements
- Docker
- Apache Kafka
- Zookeeper

### Setting up Apache Kafka and Zookeeper
You can install Apache Kafka on your machine using [official documentation](https://kafka.apache.org/documentation/#quickstart) 
or pull this Image provided on [DockerHub](https://hub.docker.com/r/johnnypark/kafka-zookeeper/) with command below:
```
docker pull johnnypark/kafka-zookeeper
``` 
and run the instance with this command:

```
docker run -d --name kafka -e ADVERTISED_HOST=127.0.0.1 --net host johnnypark/kafka-zookeeper:latest
```

### Run Producer
Build the producer dockerfile with this command:
```
docker build -t producer .  
```
and then run it with command below:
```
docker run -d --name producer --net host producer:latest  
```

> p.s: you can use `-it` to see the output and have an interactive
> container

