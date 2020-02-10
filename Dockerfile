FROM alpine:latest

RUN apk add python3

EXPOSE 53

ADD main.py /
ADD n26utils.py /
RUN pip3 install envparse 

USER root
CMD [ "python3", "./main.py" ]
