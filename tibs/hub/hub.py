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
#    hub.py
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
class Hub:
	
    def __init__(self):

    	#TODO: 
    	#     1. make sure the RabbitMQ server is running as configured
    	#     2. restore the existing message queue (for topic advertisement)
    	#     3. restore the status of Hub from the snapshot image 

		pass

    # --------------        register part      -------------- 
    def register_publisher(self):
    	print "reg_pub"
    def register_subscriber(self):
    	pass

    # -------------- publisher specific routes -------------- 
    def create_topic(self, pub_id, topic_abstraction):
        topic_id = self.__get_new_topic_id(pub_id)
        self.__push_topic_ad()
        # return upload key

    def update_topic(self, topic_id, topic_change_log):
    	self.__push_topic_ad()
    	# return upload key

    def upload_topic_content(self, upload_key):
    	#look up the mapping table of upload_key-topic_id, ex. {(uKey1 - topic1), (uKey2 - topic2)}
    	#upload topic content to Hub
    	pass

    # -------------- subscriber specific routes -------------- 
    def subscribe_topic(self, sub_id, topic_id):
        pass

    def get_topic_content(self, sub_id, topic_id):
    	pass

    # --------------      utility functions     -------------- 
    def __get_new_topic_id(self, pub_id):
    	return "topic_id"
    
    def __push_topic_ad(self):
    	pass
