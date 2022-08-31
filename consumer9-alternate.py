import pika 
from pika.exchange_type import ExchangeType

def alt_queue_callback(ch, method, properties, body):
    print(f"Received Alternate message: {body}")

def main_queue_callback(ch, method, properties, body):
    print(f"Received MainQueue message: {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='altexchange', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct,arguments={'alternate-exchange':'altexchange'})

channel.queue_declare(queue='altexchangequeue')
channel.queue_bind('altexchangequeue', 'altexchange')
channel.basic_consume(queue='altexchangequeue', auto_ack=True, on_message_callback=alt_queue_callback)


channel.queue_declare(queue='mainxchangequeue')
channel.queue_bind('mainxchangequeue', 'mainexchange', 'test')
channel.basic_consume(queue='mainxchangequeue', auto_ack=True, on_message_callback=main_queue_callback)

print("waiting for messages")
channel.start_consuming()
connection.close()
