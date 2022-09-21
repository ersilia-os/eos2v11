# imports
import sys
import os
import csv
import requests
import urllib.parse
import posixpath
import tempfile

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

root_url = "https://admetmesh.scbdd.com/"
referer = "https://admetmesh.scbdd.com/service/screening/index"
url = "https://admetmesh.scbdd.com/service/screening/cal"
static_files_url = "/static/files/filter/result/tmp/"


def get_prediction(smiles):

    sess = requests.Session()
    r1 = sess.get(url)
    csrf_token = r1.cookies["csrftoken"]

    data = {"csrfmiddlewaretoken": csrf_token, "smiles-list": [smiles], "method": 2}
    headers = {"referer": referer}

    r2 = sess.post(url, data=data, headers=headers)

    file_name = r2.text.split(static_files_url)[1].split('"')[0]
    file_url = urllib.parse.urljoin(
        root_url, posixpath.join(static_files_url, file_name)
    )

    r3 = sess.get(file_url)

    tmp_folder = tempfile.mkdtemp(prefix="ersilia-")
    tmp_file = os.path.join(tmp_folder, "output.csv")
    with open(tmp_file, "wb") as f:
        f.write(r3.content)

    R = []
    with open(tmp_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for r in reader:
            R += [r]
    return R, header


def get_predictions(smiles_list):
    R = []
    header = None
    for smiles in smiles_list:
        R_, header_ = get_prediction(smiles)
        R += R_
        if header is None:
            header = header_
    return R, header


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


with open(output_file, "w") as f:
    writer = csv.writer(f)
    is_first = True
    for smiles_chunk in chunker(smiles_list, MAX_CHUNKSIZE):
        R, header = get_predictions(smiles_chunk)
        if is_first:
            writer.writerow(header)
        for r in R:
            writer.writerow(r)
        is_first = False
