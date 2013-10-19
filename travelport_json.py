import os
import json
import csv
import sys
reader = open("/home/hackreduce/hack_data_02/CSV/part-m-00761.csv",'r');
i=0
for line in reader.readlines():
	i=i+1
	if(i > 10):
		break;
	line = line.lstrip().rstrip()
	fields = line.split(',')
	print len(fields)
	
	doc = {}
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

	if len(fields) > 25:
		doc["roundtrip"] = 1
	 
	print doc

