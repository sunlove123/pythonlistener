#!/bin/bash
oldip='54\.255\.239\.139'
newip='52\.221\.230\.29'
cd /home/ubuntu/kube_yaml
sed -i -e 's/'$oldip'/'$newip'/g' *
cd /home/ubuntu/yaml
sed -i -e 's/'$oldip'/'$newip'/g' *
cd /home/ubuntu/install_files/haproxy
sed -i -e 's/'$oldip'/'$newip'/g' *
#/home/ubuntu/python_service/kube.sh
cp /home/ubuntu/install_files/haproxy/
echo "New ip udpated in HaProxy Conf file. Please execute haproxy-install.sh to update the same in HaProxy container"
echo "/home/ubuntu/install_files/haproxy/haproxy-install.sh"
echo "Please execute the below file to update the kube services with latest Public IP"
echo "/home/ubuntu/python_service/kube.sh"
