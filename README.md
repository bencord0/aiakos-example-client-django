# Example OpenID Client app using Django

## Launching locally

```sh
$ pipenv install
$ pipenv shell
$ export SECRET_KEY=$(uuidgen)
$ export AUTH_URL=https://$(uuidgen):$(uuidgen)@sso.example.com/
$ export AUTH_SCOPE=openid,groups
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## License
example-client-django is dual-licenced; you may choose the terms of the [MIT License](LICENSE) or the [BSD 2-Clause License](LICENSE.BSD).
