# Docker container for cmatrix, mainly for introduction of docker
#
# VERSION 0.1

# Pull base image.
FROM ubuntu:14.04

# Install packages.
RUN apt-get update && \
    apt-get install -y cmatrix && \
    rm -rf /var/lib/apt/lists/*

# Define default command.
CMD ["cmatrix"]
