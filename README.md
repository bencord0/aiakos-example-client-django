# Example OpenID Client app using Django

## Launching locally

```sh
$ pip3 install -r requirements.txt
$ SECRET_KEY=x AUTH_URL=http://ea1c25ed-2da9-4c82-a921-b87cff97b646:dummy@localhost.aiakosauth.io:2121/ python3 manage.py migrate
$ SECRET_KEY=x AUTH_URL=http://ea1c25ed-2da9-4c82-a921-b87cff97b646:dummy@localhost.aiakosauth.io:2121/ gunicorn example_client_django.wsgi
```

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

## License
example-client-django is dual-licenced; you may choose the terms of the [MIT License](LICENSE) or the [BSD 2-Clause License](LICENSE.BSD).
