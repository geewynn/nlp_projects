FROM ubuntu:16.04
MAINTAINER Godwin Ekainu

RUN apt-get update \ 
  && apt-get update -y \
  && apt-get install python-pip libatlas3-base -y \
  && pip install -U pip \
  && cd /usr/local/bin \
  && pip install -U turicreate \
  && pip install flask 

COPY follower_rec follower_rec
COPY rating_model rating_model
COPY deploy.py deploy.py

ENTRYPOINT ["python3","deploy.py"]
