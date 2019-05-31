import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

if __name__ =='__main__':
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    connection = pika.BlockingConnection(pika.ConnectionParameters('c530hcp.int.thomsonreuters.com',5672,'/',credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

