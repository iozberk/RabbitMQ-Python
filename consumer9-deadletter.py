import pika 
from pika.exchange_type import ExchangeType

def dlx_queue_callback(ch, method, properties, body):
    print(f"Received DLXqueue message: {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='dlx', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='mainexchangequeue',arguments={'x-dead-letter-exchange': 'dlx', 'x-message-ttl':1000})
channel.queue_bind('mainexchangequeue', 'mainexchange','test')

channel.queue_declare(queue='dlxequeue')
channel.queue_bind('dlxequeue', 'dlx')

channel.basic_consume(queue='dlxequeue', auto_ack=True, on_message_callback=dlx_queue_callback)

print("waiting for messages")
channel.start_consuming()
connection.close()
