FROM python:3.9.13-alpine

MAINTAINER Nikoloz Naskidashvili

WORKDIR ./code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV GROUP_ID=1000 \
    USER_ID=1000

# install dependencies
RUN python -m pip install -U --force-reinstall pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --virtual build-deps build-base gcc musl-dev jpeg-dev zlib-dev \
    && apk add postgresql-dev \
    && rm -rf /var/cache/apk/*

COPY ./requirements.txt ./requirements.txt
COPY ./requirements ./requirements

RUN apk add build-base   # install the GCC, libc-dev and binutils packages (greenlet error)
RUN pip install -r requirements.txt
RUN pip install uvicorn

# copy project
COPY . .

# create user
RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

EXPOSE 8000

USER www

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]