BASE_IMAGE=grihabor/cardiac-segmentation:base


build:
	docker build . -t $(BASE_IMAGE)

push:
	docker push $(BASE_IMAGE)

pull:
	docker pull $(BASE_IMAGE)

.PHONY: build pull push
