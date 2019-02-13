CONTAINER_NAME=pdp/pvnn
CONTAINER_PORT=5000

build: Dockerfile
	docker build  -t $(CONTAINER_NAME) .

run: build
	docker run --rm=true  --net=host -p$(CONTAINER_PORT) -i -t $(CONTAINER_NAME)
