FROM python:3.6-alpine

RUN adduser -D tinyflaskblog

WORKDIR /home/tinyflaskblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN set -e; \
  apk update \
  && apk add --virtual .build-deps gcc python3-dev musl-dev libffi-dev \
  # TODO workaround start
  && apk del libressl-dev \
  && apk add openssl-dev \
  && venv/bin/pip install cryptography==2.2.2 \
  && venv/bin/pip install pymysql \
  && apk del openssl-dev \
  && apk add libressl-dev \
  # TODO workaround end
  && apk add postgresql-dev \
  && venv/bin/pip install --no-cache-dir -r requirements.txt \
  && apk del .build-deps

COPY app app
COPY blog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP blog.py
ENV FLASK_ENV docker

RUN chown -R tinyflaskblog:tinyflaskblog ./
USER tinyflaskblog

ENTRYPOINT ["./boot.sh"]
