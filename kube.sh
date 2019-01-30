#!/bin/bash
kubectl delete svc ctauthorizationservice ctdatacacheservice ctmetadataservice ctmetanodegetservice ctmetanodeloadservice ctsessionservice ctmodelhouse expertstudioservice
kubectl delete deployments ctauthorization ctdatacache ctmetadata ctmetanodeget ctnodeload ctsession ctmodelhouse ctstudio
kubectl delete hpa ctauthorization ctdatacache ctmetadata ctmetanodeget ctmodelhouse ctnodeload ctsession ctstudio 
cd /home/ubuntu/kube_yaml/
pwd
kubectl create -f ctauthorizationservice.yaml
kubectl create -f ctdatacache.yaml
kubectl create -f ctmetadata.yaml
kubectl create -f ctmetanodeloadservice.yaml
kubectl create -f ctmetanodegetservice.yaml
kubectl create -f ctsessionservice.yaml
kubectl create -f modelhouse.yaml
kubectl create -f expertstudio.yaml
