import json
from itertools import groupby
import itertools

with open('feed.json') as data_file:
    data = json.load(data_file)
list = []
a = len(data)


#Group by Exchange
key_fun = lambda k: (k['Exchange'], k['connection'], k['routing_keys'][0])
newlist = sorted(data, key=key_fun)

#Group by connection
#newlist = sorted(data, key=lambda k: k['connection'])


filterlist = []
aa = []
subgroup = {}
finaldict= []
c= 0

#the Connection needs to be changed according to the Group by key word
for key, group in itertools.groupby(newlist, key_fun):
    subgroup[key] = []
    for m in group:
	       subgroup[key].append(m)
	
for i in subgroup.keys():
	message=  subgroup[i]	
	no_of_msg  = len(subgroup[i])
	finaldict.append( { 'key':  i,
			'message': message,
			'length': no_of_msg })



print finaldict
with open("Final.json", mode='w') as f:
            f.write(json.dumps(finaldict, indent=2))

#print aa[0]

