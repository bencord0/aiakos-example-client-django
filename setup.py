from setuptools import setup, find_packages


with open('README.md') as f:
	readme = f.read()


setup(
	name='example-client-django',
	version='0.0.0',
	description="Example OpenID Connect client using Django",
	long_description=readme,
	author="Aiakos Contributors",
	author_email="aiakos@aiakosauth.com",
	url="https://gitlab.com/aiakos/example-client-django/",
	keywords="django,auth,oauth,openid,oidc,social,ldap",

	install_requires=[
		'Django>=1.11,<1.11.99',
		'dj12',
		'django-auth-oidc',
		'gevent',
		'gunicorn',
		'raven',
		'whitenoise',
	],

	extras_require={
		'MySQL': ['mysqlclient'],
		'PostgreSQL': ['psycopg2'],
	},

	packages=find_packages(),
	include_package_data=True,

	zip_safe=True,
	classifiers=[
		'Intended Audience :: System Administrators',
		'Topic :: System :: Systems Administration :: Authentication/Directory',
	]
)
