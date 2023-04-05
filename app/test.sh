#!/bin/bash

# Get the container ID
CONTAINER_ID=$(docker ps -aqf "name=aws-demo_pythonapp")
CONTAINER_IP=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_ID)

echo "$CONTAINER_IP" > container_ip.txt

