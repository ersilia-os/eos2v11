# ADMETlab 2 models for evaluation of ADMET properties
## Model identifiers
- Slug: admetlab-2
- Ersilia ID: eos2v11
- Tags: Toxicity, Tox21, ADMET

# Model description
Systematic evaluation of ADMET properties, as well as physicochemical parameters and medicinal chemistry friendliness
- Input: SMILES
- Output: ADME, Toxicity, Physicochemical property (Predicted relevant ADMET properties, Tox21 outcomes, physicochemical properties and drug-likeness. Outputs are of mixed type, including classification (labels) and continuous values.)
- Model type: Regression, Classification
- Training set: 250,000 Molecules
- Mode of training: Online

# Source code
Cite the source publication.
- Code: The model uses the web application available at https://admetmesh.scbdd.com/
- Checkpoints: N/A

# License
The GPL-v3 license applies to all parts of the repository.

# History 
- We have developed a python script that accesses the web server available at https://admetmesh.scbdd.com/ to run the predictions.
- Python `requests` is used to post the input to the server and fetch the results.
- Model was incorporated to Ersilia on 9/16/2022

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
