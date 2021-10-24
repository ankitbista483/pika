import pika, sys
from pika.amqp_object import Properties

from pika.spec import BasicProperties

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel = channel.queue_declare(queue='task_queue', durable=True)

message = ''.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange = '',
    routing_key = 'task_queue',
    body = message,
    properties = pika.BasicProperties(delivery_mode = 2))
print(" [x] sent %r" % message)
connection.close()