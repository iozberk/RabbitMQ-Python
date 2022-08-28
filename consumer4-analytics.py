# Payment Aa
import pika 
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f"ANALTTICS SERVICES - received message {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
queue= channel.queue_declare(queue='', exclusive=True) # server aligns queue name 
channel.queue_bind(queue=queue.method.queue, exchange='routing', routing_key='analyticsonly')
channel.queue_bind(queue=queue.method.queue, exchange='routing', routing_key='both')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=callback)
print("Analytics Service waiting for messages")
channel.start_consuming()
connection.close()
