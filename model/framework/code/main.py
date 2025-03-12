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
    
    

    data = {"csrfmiddlewaretoken": csrf_token, "smiles-list": smiles, "method": 2}
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
    print("smiles list in get_predictions: ")
    print(smiles_list)
    R = []
    header = None
    smiles=smiles_list[0]
    for s in smiles_list[1:]:
    	smiles=smiles+"\r\n"+s
    R_, header_ = get_prediction(smiles)
    R += R_
    if header is None:
    	header = header_
    return R, header


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))

header_dict = {
    "LogS": "logs",
    "LogD": "logd",
    "LogP": "logp",
    "Pgp-inh": "pgp_inh",
    "Pgp-sub": "pgp_sub",
    "HIA": "hia",
    "F(20%)": "f(20%)",
    "F(30%)": "f(30%)",
    "Caco-2": "caco_2",
    "MDCK": "mdck",
    "BBB": "bbb",
    "PPB": "ppb",
    "VDss": "vdss",
    "Fu": "fu",
    "CYP1A2-inh": "cyp1a2_inh",
    "CYP1A2-sub": "cyp1a2_sub",
    "CYP2C19-inh": "cyp2c19_inh",
    "CYP2C19-sub": "cyp2c19_sub",
    "CYP2C9-inh": "cyp2c9_inh",
    "CYP2C9-sub": "cyp2c9_sub",
    "CYP2D6-inh": "cyp2d6_inh",
    "CYP2D6-sub": "cyp2d6_sub",
    "CYP3A4-inh": "cyp3a4_inh",
    "CYP3A4-sub": "cyp3a4_sub",
    "CL": "cl",
    "T12": "t12",
    "hERG": "herg",
    "H-HT": "h_ht",
    "DILI": "dili",
    "Ames": "ames",
    "ROA": "roa",
    "FDAMDD": "fdamdd",
    "SkinSen": "skinsen",
    "Carcinogenicity": "carcinogenicity",
    "EC": "ec",
    "EI": "ei",
    "Respiratory": "respiratory",
    "BCF": "bcf",
    "IGC50": "igc50",
    "LC50": "lc50",
    "LC50DM": "lc50dm",
    "NR-AR": "nr_ar",
    "NR-AR-LBD": "nr_ar_lbd",
    "NR-AhR": "nr_ahr",
    "NR-Aromatase": "nr_aromatase",
    "NR-ER": "nr_er",
    "NR-ER-LBD": "nr_er_lbd",
    "NR-PPAR-gamma": "nr_ppar_gamma",
    "SR-ARE": "sr_are",
    "SR-ATAD5": "sr_atad5",
    "SR-HSE": "sr_hse",
    "SR-MMP": "sr_mmp",
    "SR-p53": "sr_p53",
    "MW": "mw",
    "Vol": "vol",
    "Dense": "dense",
    "nHA": "nha",
    "nHD": "nhd",
    "TPSA": "tpsa",
    "nRot": "nrot",
    "nRing": "nring",
    "MaxRing": "maxring",
    "nHet": "nhet",
    "fChar": "fchar",
    "nRig": "nrig",
    "Flex": "flex",
    "nStereo": "nstereo",
    "NonGenotoxic_Carcinogenicity": "nongenotoxic_carcinogenicity",
    "LD50_oral": "ld50_oral",
    "Genotoxic_Carcinogenicity_Mutagenicity": "genotoxic_carcinogenicity_mutagenicity",
    "SureChEMBL": "surechembl",
    "NonBiodegradable": "nonbiodegradable",
    "Skin_Sensitization": "skin_sensitization",
    "Acute_Aquatic_Toxicity": "acute_aquatic_toxicity",
    "Toxicophores": "toxicophores",
    "QED": "qed",
    "Synth": "synth",
    "Fsp3": "fsp3",
    "MCE-18": "mce_18",
    "Natural Product-likeness": "natural_product_likeness",
    "Alarm_NMR": "alarm_nmr",
    "BMS": "bms",
    "Chelating": "chelating",
    "PAINS": "pains",
    "Lipinski": "lipinski",
    "Pfizer": "pfizer",
    "GSK": "gsk",
    "GoldenTriangle": "goldentriangle"
}


with open(output_file, "w") as f:
    writer = csv.writer(f)
    is_first = True
    for smiles_chunk in chunker(smiles_list, MAX_CHUNKSIZE):
        R, header = get_predictions(smiles_chunk)
        if is_first:
            mapped_header = [header_dict.get(col, col) for col in header]
            writer.writerow(mapped_header)
        for r in R:
            writer.writerow(r)
        is_first = False
