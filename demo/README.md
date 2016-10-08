# Docker FTW Demo 

This is the main demo for #dockerftw. I like to think if something is built well, then
it can run itself. There are lots of examples out in the world of docker applications
running docker applications. Docker is a swiss army knife. There are many use cases
and not confining yourself to using it in just one way is a good start to understanding its power.

## Build

```docker build -t demo .```

## run

```docker run -it -e PORT=9000 -p 9000:9000 demo```
