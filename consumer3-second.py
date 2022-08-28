import pika 
from pika.exchange_type import ExchangeType
def callback(ch, method, properties, body):
    print(f"SECOND CONSUMER received message {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
queue = channel.queue_declare(queue='', exclusive=True) # empty string means server auto-generate a name 
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=callback)
print("waiting for messages")
channel.start_consuming()
connection.close()
