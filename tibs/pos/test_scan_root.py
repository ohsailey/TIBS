import os
import json 
from pprint import pprint

<<<<<<< HEAD
#for root, dirs, files in os.walk("./test_root_dir", topdown=False):
    #for name in files:
        #print(os.path.split(os.path.join(root, name))[1])'''
    #for name in dirs:
        #print(os.path.split(os.path.join(root, name))[1])
=======
>>>>>>> e2dd68628be5c05012eea4f3c671939ac538ff07
def __scan_root_path():
    metadata = __read_metadata()
    current_pos = {}
    current_pos["pos"]=[]
        pub_index = os.walk("./test_root_dir").next()[1]
    for pub_index, publisher in enumerate(pub_index) :        pub_existed = __is_publisher_existed(publisher, metadata)        if pub_existed:            pub_layer = os.path.join("./test_root_dir", publisher)            pub_topics_list = metadata["pos"][pub_index]["publisher_topics"]            current_topics = __scan_pub_path(pub_layer, pub_topics_list)            current_pos["pos"].append({
			    "pub_name":publisher,
			    "pub_id":metadata['pos'][pub_index]['publisher_id'],
				"pub_topics":current_topics
			})            print 'found ' + publisher + '\n---\n'        else:
		    print 'not found publisher'    print current_posdef __scan_pub_path(pub_layer, pub_topics_list):
    current_topics = []
    topic_index = os.walk(pub_layer).next()[1]    for topic_index, topic in enumerate(topic_index):        topic_existed = __is_topic_existed(topic, pub_topics_list)        if topic_existed:            topic_layer = os.path.join(pub_layer, topic)            topic_data_list = pub_topics_list[topic_index]["topic_data"]            current_data = __scan_topic_path(topic_layer, topic_data_list)            current_topics.append({
			    "topic_name":topic,
			    "topic_id":pub_topics_list[topic_index]['topic_id'],                "topic_data":current_data
			})            print 'found ' + topic + '\n---\n'
        else:
		    print 'not found topic'    return current_topics


def __scan_topic_path(topic_layer, data_list):
    current_data = []
    existing_data = os.walk(topic_layer).next()[1]
    for data in existing_data:        data_existed = __is_data_existed(data, data_list)
        if data_existed:            data_layer = os.path.join(topic_layer, data)            file_list = data_list["file_list"]            current_files = __scan_data_path(data_layer, file_list)            current_data.append({
<<<<<<< HEAD
                "data_name":data,
=======
                "data_name":file,
>>>>>>> e2dd68628be5c05012eea4f3c671939ac538ff07
			    "data_id":data_list["data_id"],                "file_list":current_files
			})        else:
		    print 'not found data'
    return current_data
	def __scan_data_path(data_layer, file_list):
    current_files =[]    for root, dirs, files in os.walk(data_layer):        for file in files:               file_existed = __is_file_existed(file, file_list)            if file_existed :                current_files.append({                    "file_name":file,
			        "file_id":""
			    })                print 'found' + file + '\n---\n'            else :                print 'not found file'    return current_files

def __is_publisher_existed(pub_name, r_pos_info):
    pub_list = [pub for pub in r_pos_info['pos'] if pub['publisher_name'] == pub_name]
    result = False
    if len(pub_list) > 0:
        return True
    return Falsedef __is_topic_existed(topic_name, topic_info):
    topic_list = [topic for topic in topic_info if topic['topic_name'] == topic_name]    result = False
    if len(topic_list) > 0:
        return True
    return Falsedef __is_data_existed(data_name, data_info):
    result = False    if data_name == data_info['data_name']:        return True    return Falsedef __is_file_existed(file_name, file_info):
    file_list = [file for file in file_info if file['file_name'] == file_name]
    result = False
    if len(file_list) > 0:
        return True
    return False
def __read_metadata(): 
    required_pos={}
    metadata_loc = os.path.join("./test_root_dir", "pos.metadata")
    json_data=open(metadata_loc)
    metadata = json.load(json_data)
    required_pos["pos"] = metadata["subscribe_dataset"]
    return required_pos

if __name__ == "__main__":
    __scan_root_path()
