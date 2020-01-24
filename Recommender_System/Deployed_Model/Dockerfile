FROM ubuntu:latest
MAINTAINER Godwin Ekainu

RUN apt-get update \ 
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install tensorflow \
  && pip3 install turicreate \
  && pip3 install pandas \
  && pip3 install flask 

COPY follower_rec follower_rec
COPY rating_model rating_model
COPY deploy.py deploy.py

ENTRYPOINT ["python3","deploy.py"]
