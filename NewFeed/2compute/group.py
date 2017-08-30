import json
from itertools import groupby
import itertools

with open('feed.json') as data_file:    
    data = json.load(data_file)
list = []
a = len(data)


#Group by Exchange
key_fun = lambda k: (k['Exchange'], k['connection'])
newlist = sorted(data, key=key_fun) 

#Group by connection
#newlist = sorted(data, key=lambda k: k['connection']) 

gblist=[]


#the Connection needs to be changed according to the Group by key word
for key, group in itertools.groupby(newlist, key_fun):	
	print key," : ",(group)	
	
	for j in group:
	    print j
	    print ""
	    
	 
#gblist=groupby(newlist, key=lambda k: k['Exchange'])


print ""
print "Total messages ", a
