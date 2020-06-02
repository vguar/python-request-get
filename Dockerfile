FROM python

WORKDIR /usr/src/app
ADD requirements.txt .

RUN ["pip", "install", "-r", "requirements.txt"]

ADD url-request.py .

RUN useradd -u 1001 user

USER 1001

CMD ddtrace-run /usr/local/bin/python url-request.py --url $URL