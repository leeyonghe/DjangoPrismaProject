FROM python:3.8

RUN apt update

RUN apt install nodejs -y

RUN apt install npm -y

RUN npm install -g npx

RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /main