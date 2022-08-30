# Publishing Options
import pika 
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.confirm_delivery()
channel.tx_select()
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

channel.queue_declare('Test', durable=True)

message = "Broadcast Message"



channel.basic_publish(
    exchange='pubsub', 
    routing_key='', 
    body=message, 
    properties=pika.BasicProperties(headers={'name': 'Ismail', 'age': '28'},
    delivery_mode=1,expiration=13434343,content_type='application/json'),
    mandatory=True)

channel.tx_commit()
channel.tx_rollback()

print(f"sent message {message}")
connection.close()



