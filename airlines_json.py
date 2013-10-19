import json
import csv
import sys
from itertools import izip
import os

fileIn = open('tnz_airlines', 'r')

reader = csv.reader(fileIn)

keys = ("airline_code","carrier_iata_code","carrier_icao_code","name","carrier_short_name","carrier_category")

out = []

for property in reader:
	property = iter(property)
	data = {}
	out = [dict(zip(keys, property)) for property in reader]
	out += [ data ]


#print out[0]
#pp.pprint(out)
i = 0
for d in out:
	json_data = str(d)
	json_data = json_data.replace("'", '"')
	curlCommand = "curl -XPOST http://cluster-7-slave-01.sl.hackreduce.net:9200/flight_airlines/flight-mapping/" + str(i) + " -d '" + json_data + "'"
	print curlCommand
	i += 1
	result = os.system(curlCommand)
	print result
	
