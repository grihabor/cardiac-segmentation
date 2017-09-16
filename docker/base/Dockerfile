FROM library/python:3.6-alpine
MAINTAINER Borodin Gregory <grihabor@mail.ru>


# numpy:
# - gcc
# - musl-dev

RUN apk update \
 && apk add --virtual build-deps \
    gcc \
    musl-dev \
 && pip3 install --no-cache-dir \
    numpy \
 && apk del build-deps

RUN pip3 install --no-cache-dir \
    pypng \
    pydicom

