FROM python:2.7.10
LABEL maintainer="Arthur Atrokhov <aatrokhov@gmail.com>"
ENV DJANGO_SETTINGS_MODULE mp3converter.settings
RUN pip install --upgrade pip
ADD requirements.txt /mp3converter/requirements.txt
RUN pip install -r /mp3converter/requirements.txt
ADD . /mp3converter
WORKDIR /mp3converter/