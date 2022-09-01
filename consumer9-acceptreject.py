import pika 
from pika.exchange_type import ExchangeType

def acceptreject_queue_callback(ch, method, properties, body):
    if(method.delivery_tag % 5 == 0) :
        ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)
    print(f"Received Accept-Reject message: {body}")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='acceptrejectxchange', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='letterbox')
channel.queue_bind('letterbox', 'acceptrejectxchange','test')

channel.basic_consume(queue='letterbox', on_message_callback=acceptreject_queue_callback)

print("Waiting for message")
channel.start_consuming()
connection.close()
