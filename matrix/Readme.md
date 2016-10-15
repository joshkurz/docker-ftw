# Matrix Demo

## This containerizes the matrix so we can control it and become The One.

### Run demo
```
docker run -it joshkurz/matrix
```

### Some difference between a container v image
```
# build the container
docker build .

# run matrix in the background with -d
# allocate tty with -t
docker run -t -d matrix

# execute a command in the container and get a bash shell running
# this gives us access to the internals of the running container
docker exec -it $containerid /bin/bash
touch foobar
exit

# show diff of filesystem
docker diff $containerid

# start new container
docker run -it -d matrix

# show both contianers
docker ps
# stop each container
docker stop $containerid
docker stop $containerid2
# show that both of thier instances are left over and can be restarted
docker ps -a
# remove all containers
docker rm $(docker ps -qa)
```
