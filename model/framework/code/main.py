# imports
import sys
import os
import csv
import json
import requests
import pandas as pd

MAX_CHUNKSIZE = 250

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# read smiles list
smiles_list = []
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles_list += [r[0]]


def get_predictions(smiles):

    baseUrl = 'https://admetlab3.scbdd.com'
    api = '/api/admet'
    url = baseUrl + api
    param = {'SMILES': smiles}

    response = requests.post(url, json=param)
    print(str(response))
    #data = response.json()['data']

    return ['A' for a in smiles], ['A' for a in smiles]



def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


# output results
with open(output_file, "w") as f:
    writer = csv.writer(f)
    is_first = True
    for smiles_chunk in chunker(smiles_list, MAX_CHUNKSIZE):
        R, header = get_predictions(smiles_chunk)
        if is_first:
            #mapped_header = [header_dict.get(col, col) for col in header]
            mapped_header = header
            writer.writerow(mapped_header)
        for r in R:
            writer.writerow(r)
        is_first = False
