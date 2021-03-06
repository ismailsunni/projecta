# coding=utf-8
"""Project level settings."""
from .project import *


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# Localhost:9000 for vagrant
# Changes for live site
# ['*'] for testing but not for production

ALLOWED_HOSTS = ['localhost:9000', 'changelog.linfiniti.com']

if 'raven.contrib.django' in INSTALLED_APPS:
    SENTRY_DSN = (
        'http://ed76140a38244cbc9bc8d41fbfe609ae:943ed1adc81d4c'
        '98a71b2e390a8a8f42@sentry.linfiniti.com/8')

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
        'raven.contrib.django.middleware.SentryLogMiddleware',
        #for django-audited-models
        'threaded_multihost.middleware.ThreadLocalMiddleware',
    ) + MIDDLEWARE_CLASSES

    #
    # Sentry settings - logs exceptions to a database
    LOGGING = {
        # internal dictConfig version - DON'T CHANGE
        'version': 1,
        'disable_existing_loggers': True,
        # default root logger - handle with sentry
        'root': {
            'level': 'ERROR',
            'handlers': ['sentry'],
        },
        'handlers': {
            # send email to mail_admins, if DEBUG=False
            'mail_admins': {
                'level': 'ERROR',
                # see https://docs.djangoproject.com/en/dev/releases/1
                # .4/#request-exceptions-are-now-always-logged
                #'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            # sentry logger
            'sentry': {
                'level': 'WARNING',
                'class': 'raven.contrib.django.handlers.SentryHandler',
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['sentry'],
                'propagate': False
            },
            'raven': {
                'level': 'ERROR',
                'handlers': ['mail_admins'],
                'propagate': False
            },
            'sentry.errors': {
                'level': 'ERROR',
                'handlers': ['mail_admins'],
                'propagate': False
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True
            }
        }
    }
