FROM python:3.8-alpine

LABEL maintainer="lexxxell007@gamil.com"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk --no-cache add \
    # postgresql-dev gcc python3-dev musl-dev \
    # jpeg-dev zlib-dev \
    # openssl-dev \
    # musl-dev \
    # cargo \
    # rust \
    # libffi-dev \
    # ffmpeg \
    tini

ENV APP_HOME=/home/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY . .
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache pipfile-requirements && \ 
    pipfile2req $PIP_ENV > requirements.txt && \
    pip install --no-cache -r requirements.txt

# RUN apk --no-cache add shadow 
# RUN addgroup -S bmd-gg-django && adduser -S bmd-gg-django -G bmd-gg-django
# RUN groupmod -g 1002 bmd-gg-django && usermod -u 1002 -g 1002 bmd-gg-django
# RUN chown -R bmd-gg-django:bmd-gg-django $APP_HOME
# USER bmd-gg-django

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
