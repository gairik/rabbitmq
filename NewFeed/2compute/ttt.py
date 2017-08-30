from operator import itemgetter
import itertools

mylist = [{'tpdt': '0.00', 'tmst': 45.0, 'tmdt': 45.0, 'pbc': 30, 'remarks': False, 'shift': 1, 'ebct': '0.00', 'tmcdt': '0.00', 'mc_no': 'KA20'}, 
          {'tpdt': '0.00', 'tmst': 45.0, 'tmdt': 45.0, 'pbc': 30, 'remarks': False, 'shift': 1, 'ebct': '0.00', 'tmcdt': '0.00', 'mc_no': 'KA20'}, 
          {'tpdt': '0.00', 'tmst': 55.0, 'tmdt': 55.0, 'pbc': 30, 'remarks': False, 'shift': 1, 'ebct': '0.00', 'tmcdt': '0.00', 'mc_no': 'KA23'}, 
          {'tpdt': '0.00', 'tmst': 55.0, 'tmdt': 55.0, 'pbc': 30, 'remarks': False, 'shift': 1, 'ebct': '0.00', 'tmcdt': '0.00', 'mc_no': 'KA23'},
    	  {'tpdt': '0.00', 'tmst': 55.0, 'tmdt': 55.0, 'pbc': 30, 'remarks': False, 'shift': 1, 'ebct': '0.00', 'tmcdt': '0.00', 'mc_no': 'KA21'}]

#mylist.sort(key=itemgetter("mc_no"))

for key, group in itertools.groupby(mylist, lambda item: item["mc_no"]):	
	print key," : ",list(group)
	 
