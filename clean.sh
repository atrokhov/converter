#!/bin/sh
docker ps -qa -f status=exited | xargs docker rm
docker ps -qa -f status=created | xargs docker rm
docker images -f dangling=true -q | xargs docker rmi
