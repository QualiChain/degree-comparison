FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN python -m pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]