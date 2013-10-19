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
        line = line.lstrip().rstrip()
        fields = line.split(',')

        if len(fields) > 1:

        
            date_format = "%m/%d/%Y"
            depart_dt = datetime.strptime(fields[5], date_format)
            dt_of_issue = datetime.strptime(fields[1], date_format)
            advance_booking = dpart_dt - dt_of_issue

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

            doc["days_advance"] = advance_booking.days
            doc["num_segments"] = len(fields[11].split('/')) - 1
         
            print doc