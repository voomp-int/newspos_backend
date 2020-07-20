FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy Requirement Files
COPY ./requirements.txt /requirements.txt

# Install Build Dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

# Install Application Dependencies
RUN pip install -r /requirements.txt

# Delete Build Dependencies
RUN apk del .tmp-build-deps

# Copy Application Files
RUN mkdir /app
WORKDIR /app
COPY ./newspos_backend /app

# Create New User
RUN adduser -D user
USER user