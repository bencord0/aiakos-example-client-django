set -e
virtualenv3 .upenv
. .upenv/bin/activate
pip install .[MySQL,PostgreSQL]
pip uninstall --yes example-client-django
pip freeze > requirements.txt
rm -Rf .upenv
