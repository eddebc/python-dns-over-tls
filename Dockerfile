FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip \
    ca-certificates

EXPOSE 53

ADD main.py /
ADD n26utils.py /
RUN pip3 install envparse 

USER root
CMD [ "python3", "./main.py" ]
