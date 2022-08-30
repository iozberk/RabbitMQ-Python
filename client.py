import pika 
import uuid
def callback(ch, method, properties, body):
    print(f"received message {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
reply_queue = channel.queue_declare(queue='', exclusive=True)
channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=callback)
channel.queue_declare(queue='request-queue')
message = "First message to server.py"
correlation_id = str(uuid.uuid4())
print(f"Sending request: {correlation_id}")
channel.basic_publish(exchange='', 
routing_key='request-queue', 
properties=pika.BasicProperties(
    reply_to=reply_queue.method.queue,
    correlation_id=correlation_id,),
    body=message)
print(f"Sending Client: {message}")



