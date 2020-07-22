FROM debian:stable

RUN \
   apt update -y && \
   apt install -y wget git

COPY testproject /usr/bin/testproject

RUN \
   chmod +x /usr/bin/testproject
