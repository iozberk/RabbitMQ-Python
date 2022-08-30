# Consistent Hashing Exchange
# install rabbitmq-plugins enable rabbitmq_consistent_hash_exchange
import pika 
from pika.exchange_type import ExchangeType

def callback1(ch, method, properties, body):
    print(f"queue 1 received message {body}")

def callback2(ch, method, properties, body):
    print(f"queue 2 received message {body}")
connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare('samplehashing', 'x-consistent-hash') 

channel.queue_declare(queue='letterbox1')
channel.queue_declare(queue='letterbox2')

channel.queue_bind('letterbox1', 'samplehashing', routing_key='1')
channel.basic_consume(queue='letterbox1', auto_ack=True,
    on_message_callback=callback1)

channel.queue_bind('letterbox1', 'samplehashing', routing_key='1')
channel.basic_consume(queue='letterbox1', auto_ack=True,
    on_message_callback=callback2)

print("waiting for messages")
channel.start_consuming()
connection.close()

