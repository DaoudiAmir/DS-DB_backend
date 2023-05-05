import os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'URL': os.getenv('MYSQL_URL'),
        'NAME': os.getenv('MYSQLDATABASE'),
        'USER' : os.getenv('MYSQLUSER'),
        'PASSWORD' : os.getenv('MYSQLPASSWORD'),
        'HOST' : os.getenv('containers-us-west-161.railway.app'),
        'PORT' : os.getenv('MYSQLPORT')
    }
}