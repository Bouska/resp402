# settiiiingz \o/  The competent programmer is fully aware of the strictly
# limited size of his own skull; therefore he approaches the programming task
# in full humility, and among other things he avoids clever tricks like the 
# plague.    --  Edsger W. Dijkstra

from os import path

PROJECT_PATH = path.abspath(path.split(__file__)[0])


DEBUG = True
TEMPLATE_DEBUG = DEBUG
AUTH_PROFILE_MODULE = 'user.Profile'
LOGIN_URL = '/user/login'
FORCE_SCRIPT_NAME = "" # hack for nginx
ADMINS = (('Microz', 'null@null.com'),)
MANAGERS = ADMINS
UPLOAD_LOG = '/tmp/upload_log'
UPLOAD_DIR =  '%s/documents/r' % PROJECT_PATH
USER_CHECK = 'http://www.ulb.ac.be/commons/check?_type=normal&_sid=%s&_uid=%s'
PARSING_WORKERS = 7
LOGIN_REDIRECT_URL = '/zoidberg'
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
CONVERT_PDF = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sql',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ugettext = lambda s: s

LANGUAGES = (
  ('fr', ugettext('French')),
  ('en', ugettext('English')),
)

USE_L10N = True

STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = ('%s/static/' % PROJECT_PATH,)
ALLOWED_INCLUDE_ROOTS = ('%s/templates' % PROJECT_PATH,)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'v_g654gxfo#38*ju5*@bqbxg60a95dw*vpc+t&^(q*tjzazx1%'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'www.urls'

TEMPLATE_DIRS = (
    '%s/templates' % PROJECT_PATH,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'south',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from production import *
except ImportError:
    pass

try:
    from version import VERSION
except ImportError:
    VERSION = "dev"
