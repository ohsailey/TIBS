Scenarios 
=========
 

Actors
------
* Publisher
* Hub
* POS
* Mobile client


Runtime Scenarios
-----------------

* Publisher registration

 #. Publisher sends its email address to Hub
 #. Hub sends a confirmation iink via email to the publisher
 #. Publisher clicks the confirmation link
 #. Hub returns Key and Secret to the publisher
 #. Publisher sends Key and Secret  to Hub
 #. Hub returns the publisher a token


* POS registration
 #. POS sends its email address to Hub
 #. Hub sends a confirmation iink via email to the POS
 #. POS clicks the confirmation link
 #. Hub returns Key and Secret to the POS
 #. POS sends Key and Secret  to Hub
 #. Hub returns the POS a token

* Publisher publishes a new topic

 #. Publisher sends a request of publishing a new topic
 #. Hub returns true for success and false for failure 

* Publisher updates a topic
 #. Publisher sends a request of updating a new topic
 #. Hub returns true for success and false for failure 

* Publisher deletes a topic
 #. Publisher sends a request of deleting a new topic
 #. Hub returns true for success and false for failure 

* POS browses topics
 #. POS sends a request of acquiring all topics
 #. Hub returns list of all topics

* POS subscribes a topic
 #. POS sends a request of subscribing a topic
 #. Hub returns true for success and false for failure 

* POS unsubscribes a topic
 #. POS sends a request of subscribing a topic
 #. Hub returns true for success and false for failure 

* Mobile client requests data 

 #. Mobile client sends a request of requesting data
 #. Hub returns true and data for success and false for failure 


Deployment Scenarios
--------------------
