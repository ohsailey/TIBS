<<<<<<< HEAD
#coding=utf-8

from pos import Pos
#from publisher import get_topics
=======
from pos import Pos
>>>>>>> e2dd68628be5c05012eea4f3c671939ac538ff07

# TODO: initialize a new Pos object
#       and test if it is initialized correctly

<<<<<<< HEAD
test_pos = Pos('./test_root_dir/')
=======
test_pos = Pos('./test_toot_dir/')
>>>>>>> e2dd68628be5c05012eea4f3c671939ac538ff07

#TODO: replace print to assert

publishers = test_pos.get_publishers()
print len(publishers) # 3 for current test fixture

<<<<<<< HEAD

for publisher in publishers:
    print publisher.get_name()
    #print publisher
    topics = publisher.get_topics()
    #print topics
    for topic in topics:
        print topic.get_name()
        print topic.get_version()
        print topic.get_data_profile()
=======
'''for publisher in publishers:
	topics = publisher.get_topics()
	for topic in topics:
		print topic.get_name()
		print topic.get_data_profile()'''
>>>>>>> e2dd68628be5c05012eea4f3c671939ac538ff07
