FROM ubuntu:16.04

MAINTAINER Dhiraj Godwin Ekainu

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev \
    pip install -U pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "deploy.py" ]
