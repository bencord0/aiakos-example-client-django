# Example OpenID Client app using Django

## Launching locally

```sh
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ gunicorn example_client_django.wsgi
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
