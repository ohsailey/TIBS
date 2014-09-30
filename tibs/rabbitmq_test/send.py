import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hellos')

topic_msg = {
	'topic_id':'123456',
	'topic_name' : 'topicA'
}

channel.basic_publish(exchange='',
                      routing_key='hellos',
                      body=json.dumps(topic_msg))
print " [x] Sent message"
connection.close()