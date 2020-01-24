FROM ubuntu:16.04

MAINTAINER Godwin Ekainu

RUN apt-get update \ 
  && apt-get install -y python-pip python-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip install flask \
  && pip install turicreate

COPY follower_rec follower_rec
COPY rating_model rating_model
COPY deploy.py deploy.py

ENTRYPOINT ["python","deploy.py"]
