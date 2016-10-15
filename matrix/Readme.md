# Matrix Demo

## This containerizes the matrix so we can control it and become The One.

### Run demo
```
docker run -it joshkurz/matrix
```

### Some difference between a container v image
```
docker build .
docker run -it -d matrix
docker exec -it $containerid /bin/bash
touch foobar
exit
docker diff $containerid
docker run -it -d matrix
docker ps
docker stop $containerid
docker stop $containerid2
docker rm $(docker ps -q)
```
