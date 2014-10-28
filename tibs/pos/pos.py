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

from publisher import Publisher
import os
import json

class Pos:

    def __init__(self, root_path):

        self.publishers = []
        self.root_path = root_path
        self.metadata_loc = os.path.join(self.root_path, "pos.metadata")

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

    def __read_metadata(self):

        '''The function read pos metadata and
        get subscription dataset detail.

        :returns: array<str> -- the array of pos subscriptions.
        '''
        required_pos={}
        json_data=open(self.metadata_loc)
        metadata = json.load(json_data)
        required_pos["pos"] = metadata["subscribe_dataset"]
        return required_pos

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

        '''The function walk the entire directory tree
        and use pos dictionary to store its structure.
        Also, it will find all publishers and use each of
        them to create new object.

        ex:
           {
            pos:
            [
              {
                "pub_name":pub_name1,
                "pub_id":pub_id1,
                "pub_topics":topics1
              },
              {
                "pub_name":pub_name2,
                "pub_id":pub_id2,
                "pub_topics":topics2
              },
              .
              .
            ]
           ]
        '''

        metadata = self.__read_metadata()

        current_pos = {}
        current_pos["pos"]=[]

        # use self.root_path
        pub_index = os.walk(self.root_path).next()[1]
        for pub_index, pub_name in enumerate(pub_index) :
            pub_existed = self.__is_publisher_existed(pub_name, metadata)
            if pub_existed:
                pub_id = metadata['pos'][pub_index]['publisher_id']
                pub_layer = os.path.join(self.root_path, pub_name)
                pub_topics_list = metadata["pos"][pub_index]["publisher_topics"]
                current_topics = self.__scan_pub_path(pub_layer, pub_topics_list)
                current_pos["pos"].append({
                    "pub_name":pub_name,
                    "pub_id":pub_id,
                    "pub_topics":current_topics
                })

                #declare new publisher object
                pub_abc = Publisher(pub_id, pub_name, current_topics)
                self.__add_publisher(pub_abc)

                print 'found ' + pub_name + '\n---\n'
            else:
                print 'not found publisher'
        print current_pos

    def __scan_pub_path(self, pub_layer, pub_topics_list):

        '''The function scan the publisher layer
        and use array to append each topic object.

        :param pub_layer: str -- The path of publisher.
        :param pub_topics_list: array<str> -- The array of topics from metadata.
        :returns: array<str> -- the array of topics.

        ex:
            [
              {
                "name":topic_name1,
                "id":topic_id1,
                "version": topic_version1,
                "metadata_path":topic_layer1,
                "data_list":data_list1
              },
              {
                "name":topic_name2,
                "id":topic_id2,
                "version": topic_version,
                "metadata_path":topic_layer2,
                "data_list":data_list2
              },
              .
              .
           ]
        '''
        current_topics = []
        topic_index = os.walk(pub_layer).next()[1]
        for topic_index, topic in enumerate(topic_index):
            topic_existed = self.__is_topic_existed(topic, pub_topics_list)
            if topic_existed:
                topic_layer = os.path.join(pub_layer, topic)
                topic_data_list = pub_topics_list[topic_index]["topic_data"]
                current_data = self.__scan_topic_path(topic_layer, topic_data_list)
                current_topics.append({
                    "name":topic,
                    "id":pub_topics_list[topic_index]['topic_id'],
                    "version": pub_topics_list[topic_index]['topic_version'],
                    "metadata_path":topic_layer,
                    "data_list":current_data
                })
                print 'found ' + topic + '\n---\n'
            else:
                print 'not found topic'
        return current_topics

    def __scan_topic_path(self, topic_layer, data_list):
        '''The function scan the topic layer
        and use array to append each data object.

        :param topic_layer: str -- The path of topic.
        :param data_list: array<str> -- The array of data from metadata.
        :returns: array<str> -- the array of data.

        ex:
            [
              {
                "name":data_name1,
                "file_list":file_list1,
              },
              {
                "name":data_name2,
                "file_list":file_list2,
              },
              .
              .
           ]
        '''
        current_data = []
        existing_data = os.walk(topic_layer).next()[1]
        for data in existing_data:
            data_existed = self.__is_data_existed(data, data_list)
            if data_existed:
                data_layer = os.path.join(topic_layer, data)
                file_list = data_list["file_list"]
                current_files = self.__scan_data_path(data_layer, file_list)
                current_data.append({
                    "data_name":data,
                    "file_list":current_files
                })
                print 'found ' + data + '\n---\n'
            else:
                print 'not found data'
        return current_data

    def __scan_data_path(self, data_layer, file_list):
        '''The function scan the data layer
        and use array to append each file object.

        :param data_layer: str -- The path of data.
        :param file_list: array<str> -- The array of file from metadata.
        :returns: array<str> -- the array of file.

        ex:
            [
              {
                "name":file_name1,
              },
              {
                "name":file_name2
              },
              .
              .
           ]
        '''
        current_files =[]
        for root, dirs, files in os.walk(data_layer):
            for file in files:
                file_existed = self.__is_file_existed(file, file_list)
                if file_existed :
                    current_files.append({
                        "file_name":file
                    })
                    print 'found ' + file + '\n---\n'
                else :
                    print 'not found file'
        return current_files

    def __add_publisher(self, found_publisher):
        '''The function scan the data layer
        and use array to append each file object.

        :returns: array<str> -- the array of file.

        '''
        if not found_publisher in self.publishers:
            #print found_publisher.get_id()
            self.publishers.append(found_publisher)

    def get_publishers(self):
        return self.publishers

    def __is_publisher_existed(self, pub_name, r_pos_info):
        pub_list = [pub for pub in r_pos_info['pos'] if pub['publisher_name'] == pub_name]
        result = False
        if len(pub_list) > 0:
            return True
        return False

    def __is_topic_existed(self, topic_name, topic_info):
        topic_list = [topic for topic in topic_info if topic['topic_name'] == topic_name]
        result = False
        if len(topic_list) > 0:
            return True
        return False

    def __is_data_existed(self, data_name, data_info):
        result = False
        if data_name == data_info['data_name']:
            return True
        return False

    def __is_file_existed(self, file_name, file_info):
        file_list = [file for file in file_info if file['file_name'] == file_name]
        result = False
        if len(file_list) > 0:
            return True
        return False

