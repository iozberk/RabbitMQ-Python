# Exchange to Exchange Routing
import pika 
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f"received message {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='secondexchange', exchange_type=ExchangeType.fanout)
channel.queue_declare(queue='letterbox')
channel.queue_bind(queue='letterbox', exchange='secondexchange')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=callback)
print("waiting for messages")
channel.start_consuming()
connection.close()
