FROM ubuntu:16.04

MAINTAINER Godwin Ekainu

RUN apt-get update -y
RUN apt-get install -y libstdc++6 python-setuptools
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
