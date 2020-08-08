FROM alpine:latest

RUN apk add python3 py3-pip
RUN pip3 install gunicorn

ADD . /app
RUN pip3 install /app

CMD gunicorn -w 4 twitterss.wsgi:app
EXPOSE 8000
