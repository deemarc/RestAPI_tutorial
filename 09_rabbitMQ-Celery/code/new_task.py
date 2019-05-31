import pika
import sys

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(pika.ConnectionParameters('c530hcp.int.thomsonreuters.com',5672,'/',credentials))
channel = connection.channel()
# channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent 'Hello World!'")

connection.close()