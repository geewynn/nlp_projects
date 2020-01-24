FROM ubuntu:16:04
MAINTAINER Godwin Ekainu

RUN apt-get update \ 
  && apt-get install -y python3-pip python3-dev \
  && apt-get update -y \
  && apt-get install -y python-pip python-dev libatlas-base-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install tensorflow \
  && pip install turicreate \
  && pip3 install pandas \
  && pip3 install flask 

COPY follower_rec follower_rec
COPY rating_model rating_model
COPY deploy.py deploy.py

ENTRYPOINT ["python3","deploy.py"]
