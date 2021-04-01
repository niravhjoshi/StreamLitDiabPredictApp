FROM python:3.8

WORKDIR /StreamLitApp

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /StreamLitApp

ENTRYPOINT ["streamlit","run"]

CMD [ "app.py" ]