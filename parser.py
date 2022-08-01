import os
import csv
import json

def load_data(data_folder: str):
    with open(os.path.join(data_folder, 'innatedb_all.mitab'), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)
        header[0] = header[0].replace('#', '') # remove '#' from first entry

        for row in reader:
            data = dict(zip(header, row))
            source = {x.replace('_A', ''):data[x] for x in data if ('_A' in x and data[x] != '-')} # get all cols ending in _A for source
            obj = {x.replace('_B', ''):data[x] for x in data if ('_B' in x and data[x] != '-')} # get all cols ending in _B for object
            relation = {x:data[x] for x in data if (not any(substr in x for substr in ['A', 'B']) and data[x] != '-')} # get all other cols for relation
            ret = {
                "subject": source,
                "object": obj,
                "relation": relation,
                "_id": f"{data['unique_identifier_A']}-{data['unique_identifier_B']}"
            }
            yield ret
