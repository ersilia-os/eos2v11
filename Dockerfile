FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2022.3.3
RUN pip install joblib==1.1.0

WORKDIR /repo
COPY . /repo
