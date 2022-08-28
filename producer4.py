import pika 
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic) 
# First Message
user_payments_message = "Europe payments from consumer4.py"
channel.basic_publish(exchange='mytopicexchange', routing_key='user.europe.payments', body=user_payments_message)
print(f"sent message {user_payments_message}")
# Second Message

business_order_message = "Business Order Message from consumer4.py"
channel.basic_publish(exchange='mytopicexchange', routing_key='business.europe.order', body=business_order_message)
print(f"sent message {business_order_message}")

connection.close()



