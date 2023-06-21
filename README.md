# ADMETLab-2

ADMETLab2 is the improved version of ADMETLab, a suite of models for systematic evaluation of ADMET properties. ADMETLab2 provides predictions on 17 physicochemical properties, 13 medicinal chemistry properties, 23 ADME properties, 27 toxicity endpoints and 8 toxicophore rules. The code and training data are not released, using this model posts predictions to the ADMETLab2 online server. The Ersilia Model Hub also offers ADMETLab (v1) as a downloadable package for IP-sensitive queries.

## Identifiers

* EOS model ID: `eos2v11`
* Slug: `admetlab-2`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression, Classification`
* Output: `Experimental value, Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Predicted relevant ADMET properties, Tox21 outcomes, physicochemical properties and drug-likeness. Outputs are of mixed type, including classification (labels) and continuous values.

## References

* [Publication](https://academic.oup.com/nar/article/49/W1/W5/6249611?login=false)
* [Source Code](https://admetmesh.scbdd.com/)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos2v11)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2v11.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos2v11) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://academic.oup.com/nar/article/49/W1/W5/6249611?login=false) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Proprietary license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!