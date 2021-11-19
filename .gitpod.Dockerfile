FROM python:3.7

RUN python -m pip install --upgrade pip rasa[spacy]==3.0.0rc3
