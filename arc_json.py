import json
import csv
import sys
from itertools import izip
import os



#fileIn = open('head.test', 'r')

fileIn = open(sys.argv[1], 'r')

reader = csv.reader(fileIn)

keys = ("tkt_id", "dt_of_issue", "dest_id_nbr", "orig_arpt_cd", "dest_arpt_cd", "depart_dt", "depart_tm", "arrival_dt", "arrival_tm", "point_of_org_arpt_cd", "prmry_cabin_class_cd", "route_brkout", "carr_brkout", "class_of_svc_brkout", "outbound_ind", "length_of_stay_days", "prmry_carr_cd", "avg_fare_amt", "avg_doc_amt", "newline" )

out = []

for property in reader:
	property = iter(property)
	data = {}
	out = [dict(zip(keys, property)) for property in reader]
	out += [ data ]


#print out[0]
#pp.pprint(out)
i = int(sys.argv[2])
for d in out:
	json_data = str(d)
	json_data = json_data.replace("'", '"')
	curlCommand = "curl -XPOST http://cluster-7-slave-01.sl.hackreduce.net:9200/arc/arc-mapping/" + str(i) + " -d '" + json_data + "'"
	#print curlCommand
	i += 1
	result = os.system(curlCommand)
	print result
	
