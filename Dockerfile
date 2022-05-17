from ubuntu:20.04
MAINTAINER Mariia Ryleeva
RUN apt-get update -y
COPY . /opt/e2e_gsom
WORKDIR /opt/e2e_gsom
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py
