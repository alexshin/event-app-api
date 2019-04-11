# Event-app API

This repository contains source code of simple application to get 
[Eventbrite](https://www.eventbrite.com) data via their API v3.

The application provides API based on common RESTful API versioning system (i.e. 
_/api/v1/..._, _/api/v2/..._ etc.)

**Technology stack:**

* Python 3.7 / Django 2.1
* PostgreSQL 9.6 (but it should work for every DB compatible with Django)
* Some useful Django applications.


## Installation

Setup following environment variables:

```bash
# Below is a connection URI for local environment based on docker (see /docker_compose.yaml)
export DATABASE_URL=postgresql://localroot:localrootpass@localhost:5432/app
export EVENTBRITE_OAUTH_TOKEN=XXXXXXX

# For default APP_ENVIRONMENT=dev
export APP_ENVIRONMENT=prod

# Domains should be divided be comma
export APP_CORS_WHITELIST=http://localhost,http://example.com

# It can be True or False. False is default for prod environment
export CORS_ORIGIN_ALLOW_ALL=False

```


## Overview

This Django boilerplate had been done to speed up creating new environment, installing based applications, etc.

[Go to boilerplate repository](https://github.com/alexshin/django-boilerplate)

### Specifics

The boilerplate uses some tools to make your programming process easier.

###### Docker and docker-compose

In the root of project you can find `docker-compose.yaml`. You can use it to start some infrastructural services.

All credentials which is used in development process are open and they are in docker-compose.yaml and
in dev/test settings. For production purposes I recommend to use System Environment Variables or 
some secure tools sush as Hashi Corp Vault etc.

###### Dependencies

All needed dependencies are in the root directory in file `requirements.txt`. If you will change some versions, 
please don't forget to launch tests.

###### Environment settings

The boilerplate contains three different environments:

* _Development_ - not-encrypted credentials, debug tools, api documentation etc.
* _Testing_ - it's the same as Development except debug tools and other redundant apps
* _Production_ - boilerplate doesn't contain ready to use settings cause you _REALLY NEED TO DO IT YOURSELF_

### Additional batteries

##### Django-channels

Recently almost all the projects should use real-time communication between client and server. In this case there 
are not a lot of options. Django-channels enable you to use web-sockets as simple as possible.

**Pay attention on** that you should use Daphne application server against familiar ones: UWSGI or Gunicorn.

Check for detailed information in [django-channels documentation](http://channels.readthedocs.io/en/latest/)

##### Django-guardian

This application allows you to use Object-Level-Permissions beside with Class-Level-Permissions which exists in Django by default.

If you are not aware of Django-guardian, you should check [documentation](https://django-guardian.readthedocs.io/en/stable/). It will help you with the creation of almost all applications you will be creating by Django.

##### drf-yasg

Yet Another Swagger Generator helps to generate OpenAPI schema and viewer for Django Rest Framework views. See more 
docs in [official documentation](https://drf-yasg.readthedocs.io/en/stable/index.html)

_In dev environment you can check schema by `http://127.0.0.1:8000/swagger/` or `http://127.0.0.1:8000/redoc/`_

##### django-cors-headers

Adds headers to using CORS properly way. For more information see 
[official documentation](https://github.com/ottoyiu/django-cors-headers/)

### Usage

#### Requirements

* Python 3.7
* Docker and Docker-compose (min version of Docker-compose format is 3.1)


#### Quick start

```bash
# Create project directory
mkdir -p ./Projects/new-project && cd ./Projects/new-project

# Clone this repository
git clone git@github.com:alexshin/django-boilerplate.git .

# Start database
docker-compose up -d

# Install requirements
pip install -r ./requirements.txt

# Change environment to development 
export APP_ENVIRONMENT=dev

# Traditional Django commands
./src/manage.py makemigrations -y
./src/manage.py migrate -y
```

Then you can remove git history `rm -rf ./.git`

And start your own project. Enjoy it =)


#### Working with initial data

The boilerplate contains some basic modifications to work with initial data. Django already has the same mechanism which names "fixtures". But Django's way is not really useful for real-world applications.

The functionality of boilerplate enables you to create your own fixtures using Python code (I recommend you to look at Faker and Factory Boy to make creating of Django entities more smoothly but you can do it using plain Python too).

Fixtures automatically apply after migrations in the testing environment. In other environments, you should execute console 
command `apply_migrations`.

### Contributing

You can be free to ask me questions and suggest new batteries or changes. 

**You are welcome with your pull requests** 
