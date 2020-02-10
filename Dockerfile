FROM python:3-alpine

RUN pip3 install envparse 

ADD main.py /
ADD n26utils.py /

EXPOSE 8053
USER 1001
CMD [ "python3", "./main.py" ]
