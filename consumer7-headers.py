# Headers Exchange
import pika 
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f"received message {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='headersexchange', exchange_type=ExchangeType.headers)
channel.queue_declare(queue='letterbox')
channel.queue_bind(queue='letterbox', exchange='headersexchange',arguments={'x-match':'all','name':'Ismail','age':'28'})

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=callback)
print("waiting for messages")
channel.start_consuming()
connection.close()
