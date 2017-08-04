#!/usr/bin/env python
import pika
import time, sys
import json
import io
import os


creds = pika.PlainCredentials('openstack', 'demo')
param = pika.ConnectionParameters('192.168.142.127',
				  5672,
			          '/',
				  creds)
connection = pika.BlockingConnection(param)
channel = connection.channel()



result = channel.queue_declare(exclusive=True) #Creating a new Queue
queue_name = result.method.queue


#rabbitmqctl trace_on

#binding_keys = sys.argv[1:]
binding_keys="#"

channel.queue_bind(exchange='amq.rabbitmq.trace',
                   queue= queue_name,
                   routing_key=binding_keys)


messages_dict = dict()
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch,method,properties,body):
    messages_dict["Consumer Tag"]=method.consumer_tag	
    messages_dict["message-body"]=body
    #messages_dict.update({"Queue_name":queue_name})
    messages_dict.update({"Exchange":method.routing_key})
    messages_dict.update({"Exchange_Name":method.exchange})
    messages_dict.update({"TimeStamp":properties.timestamp})
    messages_dict.update({"Correlation_id":properties.correlation_id})

    print ("-------------")
    print ("[X] Consumer Tag %r ::" % method.consumer_tag)
    print ("[X] message-body %r ::" % body)
    print ("[Y] Queue_name :: %r "% queue_name)
    print ("[Y] Exchange -  :: %r "% method.routing_key)
    print ("[Y] Exchange_Name %r:: "% method.exchange)
    print ("[Y] TimeStamp %r:: "% properties.timestamp)
    print ("[Y] Correlation_id %r:: "% properties.correlation_id)
    print ("[HeaderInfo]")
    headlist = properties.headers

    for k,v in headlist.iteritems():
        messages_dict[k]=v
        print ("%r :: %r  "%(k,v))

    print ("-------------")


    #print messages_dict
    a = []
    if not os.path.isfile("feed.json"):
        a.append(messages_dict)
        with open("feed.json", mode='w') as f:
            f.write(json.dumps(a, indent=2))

    else:
        with open("feed.json", mode='a+') as feedsjson:
            feedsjson.seek(-1,2)
            feedsjson.truncate()
            feedsjson.write(',')
            feedsjson.write(json.dumps(messages_dict, indent =2))
            feedsjson.write(']')


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
print messages_dict
channel.start_consuming()
