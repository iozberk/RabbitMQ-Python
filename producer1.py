from email import message
import pika 

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='letterbox')
message = "First message"
channel.basic_publish(exchange='', routing_key='letterbox', body=message)
print(f"sent message {message}")
connection.close()



