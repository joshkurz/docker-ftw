FROM ubuntu:14.04
RUN apt-get update && apt-get install -y python-pip && \
    apt-get install -y  python-dev libffi-dev libssl-dev socat curl && \
    pip install tweepy && \
    pip install pyOpenSSL ndg-httpsclient pyasn1
WORKDIR /files
ADD files .
ENTRYPOINT ["./run.sh"]
