import pika 

def on_request_message_received(ch, method, properties, body):
    print(f"Request received: {properties.correlation_id}")
    ch.basic_publish('',routing_key=properties.reply_to,
    body=f'Reply to {properties.correlation_id}')

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='request-queue')
channel.basic_consume(queue='request-queue', auto_ack=True, on_message_callback=on_request_message_received)
print("Starting server")
channel.start_consuming()
