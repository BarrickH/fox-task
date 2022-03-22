FROM python:3.9-alpine

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev && pip install -r $CONTAINER_HOME/requirements.txt

# CMD []