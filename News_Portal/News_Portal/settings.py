"""
Django settings for News_Portal project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

import logging


logger = logging.getLogger('django')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6ssal(jupq)hke3019786+wfc54o=6y&nasd+592@^yuxqa#0b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_filters',

    'news',
    'accounts',
    'subscriptions',

    'celery',
    'redis',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    'django_apscheduler',

    'psycopg2'
]


SITE_URL = "http://127.0.0.1:8000"


SITE_ID = 1


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "mandatory"


ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 'django.core.mail.backends.smtp.EmailBackend'
# 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "nws-portal.notifications"
EMAIL_HOST_PASSWORD = "fedyhcwotvvlvzsq"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "nws-portal.notifications@yandex.ru"

SERVER_EMAIL = "nws-portal.notifications@yandex.ru"


LOGIN_REDIRECT_URL = "/posts"


ADMINS = (
    ('Ilya', 'ilyastritskiy@yandex.ru'),
)


# указываем на URL брокера сообщений
CELERY_BROKER_URL = 'redis://localhost:6379'
# указываем на хранилище результатов выполнения задач
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# допустимый формат данных
CELERY_ACCEPT_CONTENT = ['application/json']
# метод сериализации задач
CELERY_TASK_SERIALIZER = 'json'
# метод сериализации результатов
CELERY_RESULT_SERIALIZER = 'json'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]


ROOT_URLCONF = 'News_Portal.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'News_Portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы!
        # Не забываем создать папку cache_files внутри папки с manage.py!
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    # средства форматирования
    'formatters': {
        # вывод сообщений в консоль
        'cnsl_debug': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'cnsl_warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'cnsl_error_critical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        # вывод сообщений в файлы
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'errors': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'security': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        # на почту
        'email': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
    },
    # фильтры
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    # обработчики
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true',],
            'class': 'logging.StreamHandler',
            'formatter': 'cnsl_debug',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true', ],
            'class': 'logging.StreamHandler',
            'formatter': 'cnsl_warning',
        },
        'console_error': {
            'level': 'ERROR', # + будет захватываться уровень CRITICAL,
            # поэтому отдельный обработчик под него можно не делать
            'filters': ['require_debug_true', ],
            'class': 'logging.StreamHandler',
            'formatter': 'cnsl_error_critical',
        },
        'general': {
            'level': 'INFO',
            'filters': ['require_debug_false', ],
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'formatter': 'general',
        },
        'errors': {
            'level': 'ERROR', # + будет захватываться уровень CRITICAL,
            # поэтому отдельный обработчик под него можно не делать
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter': 'errors',
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'formatter': 'security',
        },
        'email': {
            'level': 'ERROR',
            'filters': ['require_debug_false', ],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'email',
        },
    },
    # регистраторы
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'general', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors', 'email', ],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors', 'email', ],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors', ],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['errors', ],
            'propagate': True
        },
        'django.security': {
            'handlers': ['security', ],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
