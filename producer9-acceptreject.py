import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='acceptrejectxchange', exchange_type=ExchangeType.fanout)

message = "Message to consumer9-acceptreject.py"

while True:
    channel.basic_publish(exchange='acceptrejectxchange', routing_key='test', body=message)
    print(f"sent message {message}")
    input('Press Any key to continue...')

