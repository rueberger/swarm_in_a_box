.PHONY: all
all: image

.PHONY: build_image
build_image:
	docker build -t rueberger/alpine-scipy:latest -f Dockerfile ${CURDIR}

# push images
.PHONY: image
image: build_image
	docker push rueberger/alpine-scipy:latest
