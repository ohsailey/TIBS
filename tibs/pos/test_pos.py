#coding=utf-8

from pos import Pos
#from publisher import get_topics

# TODO: initialize a new Pos object
#       and test if it is initialized correctly

test_pos = Pos('./test_root_dir/')

#TODO: replace print to assert

publishers = test_pos.get_publishers()
print len(publishers) # 3 for current test fixture


for publisher in publishers:
    print publisher.get_name()
    #print publisher
    topics = publisher.get_topics()
    #print topics
    for topic in topics:
        print topic.get_name()
        print topic.get_version()
        print topic.get_data_profile()