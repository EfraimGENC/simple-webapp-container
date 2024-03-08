# A Dockerized simple web application

This is a simple web application that is built using Python Fastapi and Docker.
It has two endpoints.
The first endpoint is a simple hello world endpoint and the second endpoint is a simple "say_hello" endpoint that takes in a name and returns a greeting.

## How to run the application
Build the docker image and run the container using the following commands:
```shell
docker build -t simple-web-app .
```

Run the container using the following command:
```shell
docker run -d -p 8000:8000 simple-web-app
```