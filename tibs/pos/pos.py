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
#    pos.py
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

class Pos:

	def __init__(self, root_path):

		self.publishers = {}
		self.root_path = root_path
		
        #TODO: load POS data stored in root_path into Pos class 
        #
        # 1. check if the data resided in root_path is up-to-date to Hub's
        #    if not, sync it. 
        # 2. restore data resided in root_path into this object 
        #    through self.__add_publisher(found_publisher) 
        #
		self.__check_version_consistency()
		self.__scan_root_path()


    def __check_version_consistency(self):
    	pass

    def __scan_root_path(self):
    	# if found a valid publisher directory, 
    	# generate a publisher object through 
    	# self.__add_publisher(found_publisher)
    	# stop until walking through the 
    	# root path. 

        # After scanning the root_dir
        # temp data structure may be
        #-----------------------------
    	# current_pos = {}
    	# current_pos[publisher_id] = publisher_data (publisherObj)
    	# publisher_data[topic_id] = topic_data (topicObj)
    	# topic_data[data_id] = data (dataobj)

        current_pos = {}
        # use self.root_path 
    	for dir_name in dir_names:
    	   pub_abc = Publisher(dir_name)

    	   self.__add_publisher(pub_abc)

    def __add_publisher(self, found_publisher):
    	if not found_publisher in self.publishers:
    	    self.publishers[found_publisher.get_id()] = found_publisher

	def get_publishers(self):
		return self.publishers






	