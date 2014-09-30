# -*- coding: utf-8 -*-
#    This file is part of POS with TIBS.
#
#    POS with TIBS is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    POS with TIBS is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with POS with TIBS.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
# Module Name:
#
#    hub_server.py
#
# Abstract:
#
# Author:
#
#    Project Manager : Feng-Pu Yabg 
#    Core Team Member: Bai-Small
#
# Project:
#
#    OpenISDM
#
# -*-

from flask import Flask, request
from hub import Hub
import pika

app = Flask(__name__)
app.config.from_object('hub_config')

broker_ip = app.config['RABBITMQ_HOST']
broker_queue = app.config['QUEUE_NAME']
hub_cache_path = app.config['HUB_CACHE_PATH']
topic_file_format = app.config['TOPIC_FILE_FORMAT']


#Tip: Delegate function to Hub object

#2 - add a configuration file using app.config
#    to manage RebbitMQ server's setting (ex. IP)  

hub = Hub()

# e-mail verification
@app.route("/register_publisher", methods = ['POST'])
def register_publisher():
	pass

@app.route("/register_subscriber", methods = ['POST'])
def register_subscriber():
	pass


@app.route("/create_topic", methods = ['POST'])
def create_topic():
	#3 send message (about topic's abstraction) to RabbitMQ server
	'''ex:{
		"topic_id" : "xxaa",
		"pub_id" : "987456",
	    "topic_description" : "",
		"pub_key" : "asdfghjk123456"
	}'''
	topic_msg = request.args
	if topic_msg.get("pub_key") in pub_key_list:
		send_broker(topic_msg)
	pass

@app.route("/update_topic", methods = ['POST'])
def update_topic():
	#3 send message (about topic's change log) to RabbitMQ server
	'''ex:{
		"topic_id" : "xxaa",
		"pub_id" : "987456",
	    "update_description" : "",
		"pub_key" : "asdfghjk123456",
		"change_log" : ""
	}'''
	update_msg = request.args
	
	if update_msg.get("pub_key") in pub_key_list and update_msg.get("topic_id") in topic_id_list:
		send_broker(update_msg)
	pass

@app.route("/upload_topic_content", methods = ['POST'])
def upload_topic_content():
	#4 one POST parameter is the upload key
	# upload topic content
	'''ex:{
		"topic_id" : "xxaa",
		"upload_key" : "qwertyuiop"
	}'''
	upload_msg = request.args
	if upload_key in upload_key_list:
		f = request.files['file']
		file_path = hub_cache_path + '/'+ upload_msg.get('topic_id') + topic_file_format
		f.save(file_path)
		return 'Receive success!!'
	#pass

@app.route("/subscribe_topic", methods = ['POST'])
def subscribe_topic():
	pass

@app.route("/get_topic_content", methods = ['POST'])
def get_topic_content():
	pass
	
def send_broker(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = broker_ip))
		
	channel = connection.channel()
	channel.queue_declare(queue=broker_queue)
	
	channel.basic_publish(exchange='',
                      routing_key='hellos',
					  body=msg)
                      #body=json.dumps(msg))
	print " [x] Sent message"
	connection.close()



if __name__ == "__main__":
    app.run(port=8080, debug=True)
