FROM python:3.6

WORKDIR /app
ENV PYTHONPATH /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

RUN SECRET_KEY=x ./manage.py collectstatic --noinput
CMD ["gunicorn", "-k", "gevent", "-b", "[::]:80", "example_client_django.wsgi"]
EXPOSE 80
