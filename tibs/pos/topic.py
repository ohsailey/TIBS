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
#    topic.py
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

class Topic:

	def __init__(self):
		self.data_set = []

    def get_publisher(self):
    	pass

    def get_id(self):
    	pass

	def get_name(self):
		pass

    def get_tags(self):
    	pass

    def get_version(self):
    	pass

	def get_data_profile(self):
		# 1. data description
		# 2. data_id
		#
		# current version: only data file names
		pass

	def add_data(data_obj):
		self.data_set.append(data_obj)

	def get_data(data_id):
		# 1. check data accountiability
		# 2. delegate to accountiability function (provided by publisher)
		# 3. if success, return data and save accountiability record
		#     else, return nothing and save accountiability record  
		pass
