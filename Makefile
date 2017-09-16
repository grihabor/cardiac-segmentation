all: build run

build:
	cd docker; docker-compose build segmentation

run:
	cd docker; docker-compose run segmentation

.PHONY: build run
