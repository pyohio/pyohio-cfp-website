PyOhio Website
==============

The website for PyOhio is a Django application with Symposion and Registrasion.

It is a fork of the [North Bay Python website](https://github.com/northbaypython/website) (thanks NBPy folks!)

## Setup

### Development

python 2.7.14
Django 1.11.9

1. python -m virtualenv pyohio-website
2. cd pyohio-website; 
3. git clone [your fork url] pyohio-webiste
4. cd pyohio-website
5. pip install -r requirements/base.txt
6. python manage.py migrate
7. python manage.py loaddata fixtures/*
8. python manage.py loaddata fixturesdev/*
9. python manage.py createsuperuser
10. python manage.py runserver

### Prod

Use `pip install -r requirements.txt` instead and do not install the development fixtures.

## Reference Material

* Registrasion docs are at http://registrasion.readthedocs.io
* Symposion docs are at http://symposion.readthedocs.io
