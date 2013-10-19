import os
import json
import csv
import sys
from datetime import datetime

if len( sys.argv ) < 2: 
    print "You must provide a file path" 
    sys.exit(0)
file_path = os.path.abspath( sys.argv[1]) 
reader = open(file_path,'r');
i=0
for line in reader.readlines():
        i=i+1
        if(i > 5):
                break;
	if(i < 2):
		continue;
        line = line.lstrip().rstrip()
        fields = line.split(',')
        if len(fields) > 1:

		dtfields = fields[5].split('-')
		sdate = int(dtfields[0].strip() + dtfields[1].strip() + dtfields[2].strip())
		sedate=int(dtfields[0].strip() + "1231")

		edtfields = fields[1].split('-')
		edate = int(edtfields[0].strip() + edtfields[1].strip() + edtfields[2].strip())
		esdate  = int(edtfields[0].strip() + "0101")

		advance_booking = (sedate - sdate + (edate - esdate))


		doc = {}
		doc["tkt_id"] = fields[0]
		doc["dt_of_issue"] = fields[1]
		doc["dest_id_nbr"] = fields[2]
		doc["orig_arpt_cd"] = fields[3]
		doc["dest_arpt_cd"] = fields[4]
		doc["depart_dt"] = fields[5]
		doc["depart_tm"] = fields[6]
		doc["arrival_dt"] = fields[7]
		doc["arrival_tm"] = fields[8]
		doc["point_of_orig_arpt_cd"] = fields[9]
		doc["prmry_cabin"] = fields[10]
		doc["route_brkout"] = fields[11]
		doc["carr_brkout"] = fields[12]
		doc["avg_doc_amt"] = fields[18]
		doc["avg_fare_amt"] = fields[17]

		doc["days_advance"] = advance_booking
		doc["num_segments"] = len(fields[11].split('/')) - 1

	        json_str='{"source": "' + doc["s"] + '", '
		json_str +='"destination": "' + doc["d"] + '", ' \
			'"currency": "' +  doc["cur"] + '", ' \
			'"legs":' + str(doc["nstop"]) + ', '\
			'"price":"' +  doc["price"] + '", ' \
			'"tax":"' +  doc["tax"] + '", ' \
			'"cabin": "' +  doc["cabin"] + '", ' \
			'"
		 
		json_str +='"sdate":' +  doc["arrival_dt"] + ', ' \
			'"edate":' + str( doc["depart_dt"]) + ', ' \
			'"stime":' + str( doc["arrival_tm"]) + ', ' \
			'"etime":' + str( doc["depart_tm"])  + ', ' \
			'"rt":' + str(doc["rt"]) + '}'
	
		pp.pprint(json_str)
	
		curlCommand = "curl -XPOST http://cluster-7-slave-01.sl.hackreduce.net:9200/travelport/entry_type/" + str(i) + " -d '" + json_str + "'"
#		pp.pprint(curlCommand)

		print curlCommand
		result = os.system(curlCommand)		
		print result
