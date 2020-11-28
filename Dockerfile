FROM alpine:latest
RUN apk add --no-cache bash
RUN apk add --no-cache screen
RUN apk add --no-cache python3
#RUN apk add --no-cache flask
ADD ./get-pip.py /tmp
RUN python3 /tmp/get-pip.py
RUN pip3 install flask
RUN pip3 install pyserial
RUN mkdir /app
EXPOSE 80
