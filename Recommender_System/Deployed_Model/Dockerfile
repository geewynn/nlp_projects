FROM ubuntu:16.04

MAINTAINER Godwin Ekainu

#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev \
#    pip install -U pip

RUN apt-get update && \
	apt-get install python-pip libatlas3-base -y && \
	pip install -U pip \
        pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "deploy.py" ]
