#!/bin/bash
echo "Installing RabbitMQ"

echo "removing previous rabbitmqdocker container"
docker stop rabbitmq
echo "intalling pika"
pip install pika
apt-get update
apt-get -y upgrade
echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | sudo apt-key add -
apt-get update
apt-get install rabbitmq-server
rabbitmq-plugins enable rabbitmq_management
rabbitmqctl trace_on
rabbitmqctl add_user openstack demo
rabbitmqctl set_user_tags openstack administrator
rabbitmqctl set_permissions -p / openstack ".*" ".*" ".*"
git clone https://gitlab.inria.fr/apollo/osp-parse
cd osp-parse
python feed.py


