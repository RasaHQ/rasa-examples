FROM python:3.7

RUN python -m pip install rasa

RUN python -m pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
