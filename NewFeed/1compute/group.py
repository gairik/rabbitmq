import json


with open('feed.json') as data_file:    
    data = json.load(data_file)
list = []

len1 = len(data)

c = 0
for i in data:
    a = i.pop('Exchange')
    if a == 'publish.reply_be6f5c993cf3458da21a11ed8436d378':
	c+=1
	list.append(i)

for j in list:
    print j

print "[X] Exchange Type ", a

print "[X] Total number of Exchanges ", c

print ("[X] Total number of messages ", len1)
