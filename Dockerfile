FROM python:3.11.1-slim-bullseye

RUN apt-get update \
    # lipq-dev and gg for psycopg2 build
    && apt-get install -y libpq-dev gcc libjpeg62-turbo-dev zlib1g-dev \
    libwebp-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install pip-tools==6.12.2

# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app

COPY requirements.* /app/

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 80
CMD uwsgi --http=0.0.0.0:80 --module=wsgi --ignore-sigpipe --ignore-write-errors --disable-write-exception