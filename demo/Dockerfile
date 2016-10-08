FROM golang:1.6

WORKDIR /work

# Install beego and the bee dev tool
RUN go get github.com/caarlos0/env

ADD . .
# Set the entry point of the container to the bee command that runs the
# application and watches for changes
CMD ["go", "run", "main.go"]
