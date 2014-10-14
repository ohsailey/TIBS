
# TODO: initialize a new Pos object
#       and test if it is initialized correctly


test_pos = Pos('./test_toot_dir/')

#TODO: replace print to assert

publishers = test_pos.get_publishers()
print len(publishers) # 3 for current test fixture

for publisher in publishers:
	topics = publisher.get_topics()
	for topic in topics:
		print topic.get_name()
		print topic.get_data_profile()
