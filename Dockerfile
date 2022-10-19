FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python3.10 python3.10-dev python3-pip
RUN apt-get install -y sshpass

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED 1
CMD ["python3", "main.py"]