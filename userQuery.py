import elasticsearch
import pprint 
if __name__ == "__main__":
	pp = pprint.PrettyPrinter(indent=4)
        es = elasticsearch.Elasticsearch()
        es = elasticsearch.Elasticsearch(["cluster-7-slave-01.sl.hackreduce.net:9200"], sniff_on_start=False)

	es.get(index="travelport", doc_type="entry_type", id=1)

	results = es.search(index="travelport", body = 
	{ 
		"size": "7364415", 
		"query": 
			{"match": 
				{
                                 "destination": "LGA"
                                } 
			}
	}
	)
	f = open('result.csv', 'w');
	delim = ", "
	i =0;
	for result in results["hits"]["hits"]: 
		i=i+1
	
#		print result
		esscore = result["_score"]
		strtp = ""		
		keystr = ""
	        for key in sorted(result["_source"].iterkeys()):
			if i == 1:
				keystr += key + ","
				
			strtp += str(result["_source"][key]) + ","
		keystr += "\n"
		if i==1:
			f.write(keystr)
		strtp += "\n"
                f.write(strtp)
