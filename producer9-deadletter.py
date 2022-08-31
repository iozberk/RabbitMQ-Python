import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct)

message = "Message to consumer9-DeadLetter.py (will expire)"
channel.basic_publish(exchange='mainexchange', routing_key='test', body=message)
print(f"sent message {message}")
connection.close()

