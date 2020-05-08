FROM python:alpine

WORKDIR /usr/src/app
ADD requirements.txt .

RUN apk add curl bind-tools bash

RUN ["pip", "install", "-r", "requirements.txt"]

ADD url-request.py .

RUN adduser -D --uid 1001 user
USER 1001

CMD /usr/local/bin/python url-request.py --url $URL