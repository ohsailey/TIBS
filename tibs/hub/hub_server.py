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

from flask import Flask
from hub import Hub


app = Flask(__name__)
app.config.from_object('hub_config')

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
	pass

@app.route("/update_topic", methods = ['POST'])
def update_topic():
	#3 send message (about topic's change log) to RabbitMQ server
	pass

@app.route("/upload_topic_content", methods = ['POST'])
def upload_topic_content():
	#4 one POST parameter is the upload key
	# upload topic content
	
	pass

@app.route("/subscribe_topic", methods = ['POST'])
def subscribe_topic():
	pass

@app.route("/get_topic_content", methods = ['POST'])
def get_topic_content():
	pass



if __name__ == "__main__":
    app.run(port=8080, debug=True)
