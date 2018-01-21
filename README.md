PyOhio Website
==============

The website for PyOhio is a Django application with Symposion and Registrasion.

It is a fork of the [North Bay Python website](https://github.com/northbaypython/website) (thanks NBPy folks!)

## Setup

### Development

1. pip install -r requirements/base.txt
2. python manage.py migrate
3. python manage.py loaddata fixtures/*
4. python manage.py loaddata fixturesdev/*
5. python manage.py createsuperuser
6. python manage.py runserver

### Prod

Use `pip install -r requirements.txt` instead.

## Reference Material

* Registrasion docs are at http://registrasion.readthedocs.io
* Symposion docs are at http://symposion.readthedocs.io
