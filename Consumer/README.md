# Kafka Epoch Consumer
The consumer that reads from 'input' topic, that we had on producer, transforms input message to date string (in RFC 3339) and sends to topic 'output'.
### Pre Requirements
- Docker
- Kafka Epoch Producer

> You should have Apache Kafka service and producer up and running to get the result


### Run Consumer
Build the producer dockerfile with this command:
```
docker build -t consumer .  
```
and then run it with command below:
```
docker run -d --name producer --net host consumer:latest  
```
> p.s: you can use `-it`  to see the output and have an interactive
> container
