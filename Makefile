.PHONY: help build up down logs shell test clean

help:
    @echo "Available commands:"
    @echo "  make build    - Build Docker images"
    @echo "  make up       - Start Jupyter notebook server"
    @echo "  make down     - Stop all containers"
    @echo "  make logs     - View container logs"
    @echo "  make shell    - Open shell in dev container"
    @echo "  make test     - Run tests"
    @echo "  make clean    - Remove containers and images"

build:
    docker-compose build

up:
    docker-compose up jupyter

down:
    docker-compose down

logs:
    docker-compose logs -f

shell:
    docker-compose run --rm dev /bin/bash

test:
    docker-compose run --rm test

clean:
    docker-compose down -v
    docker system prune -f
