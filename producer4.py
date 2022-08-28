import pika 
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
message = "Message from consumer4.py"
channel.basic_publish(exchange='routing', routing_key='both', body=message)
print(f"sent message {message}")
connection.close()



