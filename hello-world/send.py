import pika
from pika.credentials import PlainCredentials
from pika.spec import Channel, Queue

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
Channel = connection.channel()

Channel.queue_declare(queue = 'hello')

Channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()