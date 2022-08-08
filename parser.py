import os
import csv
import json
from collections import Counter

# input: "psi-mi:\"MI:0415\"(enzymatic study)"
# output: {
#   "psi-mi": "MI:0415",
#   "label": "enzymatic study"
# }
def separate_id_and_label(line):
    id_and_label = line.split('\"')
    return {
        "psi-mi": id_and_label[1],
        "label": id_and_label[2].replace(')', '').replace('(', '')
    }

# input: "lpr:1|hpr:1|np:1|"
# output: {
#   "lpr": 1,
#   "hpr": 1,
#   "np": 1
# }
def separate_confidence_score(line):
    confidence_scores = [x for x in line.split('|') if x]
    return {
        x.split(':')[0]: int(x.split(':')[1]) for x in confidence_scores
    }

# input: "uniprotkb:ISK5_HUMAN|uniprotkb:Q9NQ38|refseq:NP_001121170|refseq:NP_006837|refseq:NP_001121171|hgnc:SPINK5(display_short)"
# output: {
#   "uniprotkb_name": "ISK5_HUMAN"
#   "uniprotkb": ["Q9NQ38"],
#   "refseq": ["NP_001121170", "NP_006837", "NP_001121171"],
#   "hgnc_name": "SPINK5"
# }
def separate_alias(line):
    uniprotkb_name = [x for x in line.split('|') if ('_HUMAN' in x or '_MOUSE' in x)]
    hgnc_name = [x for x in line.split('|') if '(display_short)' in x]
    alias = [x for x in line.split('|') if x not in uniprotkb_name and x not in hgnc_name]

    #convert alias to dict of lists based on type
    alias_dict = {}
    for x in alias:
        if x.split(':')[0] in alias_dict:
            alias_dict[x.split(':')[0]].append(x.split(':')[1])
        else:
            alias_dict[x.split(':')[0]] = [x.split(':')[1]]
    
    if uniprotkb_name:
        alias_dict['uniprotkb_name'] = uniprotkb_name[0].replace('uniprotkb:', '')

    if hgnc_name:
        alias_dict['hgnc_name'] = hgnc_name[0].replace('(display_short)', '').replace('hgnc:', '')
        
    return alias_dict    

def process_node(obj):
    obj['unique_identifier'] = {"innatedb": obj['unique_identifier'].replace('innatedb:', '')}
    obj['alt_identifier'] = {"ensembl": obj['alt_identifier'].replace('ensembl:', '')}
    obj['alias'] = separate_alias(obj['alias'])
    obj['ncbi_taxid'] = int(obj['ncbi_taxid'].replace('taxid:', '').split('(')[0]) # extract number
    for k in ['biological_role', 'exp_role', 'interactor_type', 'participant_identification_method']:
        if k in obj:
            obj[k] = separate_id_and_label(obj[k])

    return obj

def process_relation(relation):
    relation['interaction_detection_method'] = separate_id_and_label(relation['interaction_detection_method'])
    relation['interaction_type'] = separate_id_and_label(relation['interaction_type'])
    relation['pmid'] = int(relation['pmid'].replace('pubmed:', ''))
    relation['confidence_score'] = separate_confidence_score(relation['confidence_score'])
    relation['ncbi_taxid_host_organism'] = int(relation['ncbi_taxid_host_organism'].replace('taxid:', ''))
    relation['creation_date'] = relation['creation_date'].replace('/', '-')
    relation['update_date'] = relation['update_date'].replace('/', '-')
    return relation

def load_data(data_folder: str):
    count = Counter()
    with open(os.path.join(data_folder, 'innatedb_all.mitab'), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)
        header[0] = header[0].replace('#', '') # remove '#' from first entry

        for row in reader:
            data = dict(zip(header, row))
            source = {x.replace('_A', ''):data[x] for x in data if ('_A' in x and data[x] != '-')} # get all cols ending in _A for source
            obj = {x.replace('_B', ''):data[x] for x in data if ('_B' in x and data[x] != '-')} # get all cols ending in _B for object
            relation = {x:data[x] for x in data if (not any(substr in x for substr in ['A', 'B']) and data[x] != '-')} # get all other cols for relation

            id = f"{data['unique_identifier_A']}_{data['unique_identifier_B']}_{relation['idinteraction_in_source_db']}"
            count[id] += 1

            ret = {
                "subject": process_node(source),
                "object": process_node(obj),
                "relation": process_relation(relation),
                "_id": f"{id}_{count[id]}" if count[id] > 1 else id
            }
            yield ret
            