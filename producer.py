import pika

connection_parameters = pika.ConnectionParameters(host='localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

message = 'Hello World!'

channel.basic_publish(exchange='', routing_key='hello', body=message)

print(f'sent message: {message}')

connection.close()