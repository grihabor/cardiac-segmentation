FROM library/python:3.6-alpine
MAINTAINER Borodin Gregory <grihabor@mail.ru>


# numpy:
# - gcc
# - musl-dev
# scikit-image:
# - freetype-dev
# - libpng-dev

RUN apk update \
 && apk add --virtual build-deps \
    gcc \
    musl-dev \
    freetype-dev \
    libpng-dev \
 && pip3 install --no-cache-dir \
    pydicom \
    numpy \
    scikit-image \
 && apk del build-deps


