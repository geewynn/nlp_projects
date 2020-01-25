FROM ubuntu:16.04

MAINTAINER Godwin Ekainu

RUN apt-get update && \
    apt-get install -y python-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
