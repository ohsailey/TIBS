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


class Publisher:

	def __init__(self, pid, pname):
		self.id = pid
		self.name = pname
		self.topics = {}

	def get_id():
		return self.id

	def get_name():
		return self.name

	def get_topics(self):
		pass


	def add_topic(self, topic):
		self.topics[topic.get_topic_id] = topic

