from enum import auto
import pika

def on_message_received(channel, method, properties, body):
    print(f'received message: {body}')

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(queue='hello', auto_ack = True, on_message_callback=on_message_received)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()