FROM python:3
USER root

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN apt-get update && \
    apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt install -y vim less wget git unzip && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install poetry
