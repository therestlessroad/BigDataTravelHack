import csv
import json
from itertools import izip
f = open( '/u01/teams/slavedata/amadeus/20110901_subset.csv', 'r' )
reader = csv.reader( f )
keys= ( "Date", "Time", "Origin", "Destination", "Round", "NbSegments" )
out = []
for property in reader:
    property = iter( property )
    data = {}
    out = [dict(zip(keys, property)) for property in reader]
    out += [ data ]
print json.dumps(out)
