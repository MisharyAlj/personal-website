from .base import *

import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7-u^#qq%wolcakd+^=of4d0-h3p@e6m3j&43fl6ce&ngrt21h7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = 'static/'

# Base url to serve media files
MEDIA_URL = 'media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
