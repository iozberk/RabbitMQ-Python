# Consistent Hashing Exchange
import pika 

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare('samplehashing', 'x-consistent-hash')
routing_key = "HASHING"
message = "This message is sent with hashing"
channel.basic_publish(
    exchange='samplehashing', 
    routing_key=routing_key, 
    body=message)
print(f"sent message {message}")
connection.close()



