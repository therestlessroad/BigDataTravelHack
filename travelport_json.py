import os
import json
import csv
import sys
from os import listdir
from os.path import isfile, join
import elasticsearch
import pprint 

pp = pprint.PrettyPrinter(indent=4)

dirPath = "/home/hackreduce/hack_data_02/CSV/"
#onlyfiles = [ f for f in listdir(dirPath) if isfile(join(dirPath, f)) ]
#reader = open("/home/hackreduce/hack_data_02/CSV/part-m-00761.csv",'r');
es = elasticsearch.Elasticsearch()
es = elasticsearch.Elasticsearch(["cluster-7-slave-00.sl.hackreduce.net:9200"], sniff_on_start=False)
j=0
onlyfiles = ["part-m-00761.csv"]
for tfile in onlyfiles:
	print tfile
	j=j+1
	if(j > 1):
	 	break
	tmpFile = join(dirPath, tfile)
	reader = open(tmpFile, 'r')
	i=0
	for line in reader.readlines():
		i=i+1
		if(i > 10):
			break;
		line = line.lstrip().rstrip()
		fields = line.split(',')
		
		doc = {}
		doc["id"] = i
		legs= (fields[6].split('|'))
		doc["s"] = legs[0]
		doc["d"] = (fields[7].split('|'))[-1]
		sdatetime = (fields[8].split('|'))[0]
		(sd, st) = divmod(int(sdatetime), 10000)
		doc["sd"] = sd
		doc["st"] = st
		edatetime = (fields[9].split('|'))[-1]
		(dd, dt) = divmod(int(edatetime), 10000)
		doc["dd"] = dd
		doc["dt"] = dt
		doc["nstop"] = len(legs)-1
		doc["cur"] = fields[0]
		doc["price"] = fields[1]
		doc["tax"] = fields[2]
		cabinInfo = fields[16].split('|')

		for c in cabinInfo:
			if c == 'F':
				doc["cabin"] = "F"
				break
			elif c == 'B':
				doc["cabin"] = "B"
				break
			else:
				doc["cabin"] = "E"
		print doc["cabin"]
		if len(fields) > 25:
			doc["rt"] = 1
		 
	#		result = es.index("travelport1+", "type1",
		json_str='{"source": "' + doc["s"] + '", '
		json_str +='"destination": "' + doc["d"] + '", ' \
			'"currency": "' +  doc["cur"] + '", ' \
			'"legs":' + str(doc["nstop"]) + ', '\
			'"price":"' +  doc["price"] + '", ' \
			'"tax":"' +  doc["tax"] + '", ' \
			'"cabin": "' +  doc["cabin"] + '", '
		 
		json_str +='"sdate":' +  str(doc["sd"]) + ', ' \
			'"edate":' + str( doc["dd"]) + ', ' \
			'"stime":' + str( doc["st"]) + ', ' \
			'"etime":' + str( doc["dt"])  + ', ' \
			'"rt":' + str(doc["rt"]) + '}'
	
		pp.pprint(json_str)
	
		curlCommand = "curl -XPOST http://cluster-7-slave-01.sl.hackreduce.net:9200/travelport/entry_type/" + str(i) + " -d '" + json_str + "'"
#		pp.pprint(curlCommand)

		print curlCommand
		result = os.system(curlCommand)		
		print result
