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

import os
import json

class Topic:

    def __init__(self, tid, tname, topic_version, root, t_data):
        self.id = tid
        self.name = tname
        self.version = topic_version
        self.root = root
        self.data_set = t_data
        self.data_profile = self.__read_metadata()


    def get_publisher(self):
        pass

    def get_id(self):
        return self.id

   
    #next iteration

    def get_name(self):
        return self.name

    def get_tags(self):
        pass

    def get_version(self):
        return self.version

    def get_data_profile(self):
        # 1. data description (from metadata)
        # 2. data_id (from metadata)
        # 3. data_name
        # 4. accountability_name (from metadata)
        # 5. accountability_description (from metadata)
        #
        # TODO: read metadata and write self.data_profile
        return self.data_profile


    def get_data(data_id):
        # 1. check data accountability
        # 2. delegate to accountability function (provided by publisher)
        # 3. if success, return data and save accountability record
        #     else, return nothing and save accountability record

        data = self.data_profile[data_id]
        #data-level
        data_acc_desc = data['accountability_description']
        data_acc_name = data['accountability_name']
        data_description = data['description']
        #object-level
        data_object_names = data['object_names']
        data_object_descriptions = data['object_descriptions']

    def __read_metadata(self):
        #TODO:
        #  Error checking:
        #                1. no metadata
        #                2. mismatch between t_data & scanned result
        if self.__err_detector_metadata_data_mismatch():
            self.__err_handler_metadata_data_mismatch()
        if self.__err_detector_no_metadata():
            self.__err_handler_no_metadata()

        path = os.path.join(self.root, "data.metadata")
        json_data=open(path)
        metadata = json.load(json_data)

        return metadata

        #TODO: read metadata
        #      ...

    def __err_detector_metadata_data_mismatch(self):
        pass

    def __err_detector_no_metadata(self):
        pass

    def __err_handler_metadata_data_mismatch(self):
        pass

    def __err_handler_no_metadata(self):
        pass
