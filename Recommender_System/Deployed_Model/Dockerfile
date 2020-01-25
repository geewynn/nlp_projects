FROM ubuntu:18.04

MAINTAINER Godwin Ekainu

RUN sudo apt-get install libgconf-2-4
RUN sudo apt-get install -y libstdc++6 python-setuptools
RUN sudo easy_install pip
RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
