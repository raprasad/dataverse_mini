"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *

# Store uploaded files, logs, etc, etc
TEST_SETUP_DIR = join(dirname(DJANGO_ROOT), 'test_setup')

STATIC_ROOT =join(TEST_SETUP_DIR, 'assets') # where files gathered and served from

MEDIA_ROOT = join(TEST_SETUP_DIR, 'media' )

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(TEST_SETUP_DIR, 'db', 'miniverse2014.db3')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
   
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    #'debug_toolbar',
    #'djcelery',
    #'kombu.transport.django', 
)

MIDDLEWARE_CLASSES += (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION

########## SESSION_COOKIE_NAME
SESSION_COOKIE_NAME = 'dataverse_mini'
########## END SESSION_COOKIE_NAME

########## DV_DATAFILE_DIRECTORY
DV_DATAFILE_DIRECTORY = join(TEST_SETUP_DIR, 'dv_datafile_directory')
########## END DV_DATAFILE_DIRECTORY
