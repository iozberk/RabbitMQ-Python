import pika 
import time
import random
def callback(ch, method, properties, body):
    processing_time = random.randint(1,6) # Random processing time between 1 and 6 seconds
    print(f"received message {body}, will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing message")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='letterbox')
#channel.basic_qos(prefetch_count=1) second consumer will not receive messages until first consumer has finished processing
channel.basic_consume(queue='letterbox', on_message_callback=callback)
print("waiting for messages")
channel.start_consuming()
connection.close()
