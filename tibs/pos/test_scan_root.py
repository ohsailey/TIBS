import os
import json 
from pprint import pprint

def __scan_root_path():
    metadata = __read_metadata()
    current_pos = {}
    current_pos["pos"]=[]
    
    for pub_index, publisher in enumerate(pub_index) :
			    "pub_name":publisher,
			    "pub_id":metadata['pos'][pub_index]['publisher_id'],
				"pub_topics":current_topics
			})
		    print 'not found publisher'
    current_topics = []
    topic_index = os.walk(pub_layer).next()[1]
			    "topic_name":topic,
			    "topic_id":pub_topics_list[topic_index]['topic_id'],
			})
        else:
		    print 'not found topic'


def __scan_topic_path(topic_layer, data_list):
    current_data = []
    existing_data = os.walk(topic_layer).next()[1]
    for data in existing_data:
        if data_existed:
                "data_name":file,
			    "data_id":data_list["data_id"],
			})
		    print 'not found data'
    return current_data
	
    current_files =[]
			        "file_id":""
			    })

def __is_publisher_existed(pub_name, r_pos_info):
    pub_list = [pub for pub in r_pos_info['pos'] if pub['publisher_name'] == pub_name]
    result = False
    if len(pub_list) > 0:
        return True
    return False
    topic_list = [topic for topic in topic_info if topic['topic_name'] == topic_name]
    if len(topic_list) > 0:
        return True
    return False
    result = False
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