"""
Django settings for whatsappbot project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import django_heroku
from decouple import config,Csv
import dj_database_url

MODE=config("MODE", default="dev")
SECRET_KEY = config('SECRET_KEY')
WHATSAPP_TOKEN = os.environ['WHATSAPP_TOKEN']

DEBUG = True
# development
# if config('MODE')=="dev":
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2',
#            'NAME': config('DB_NAME'),
#            'USER': config('DB_USER'),
#            'PASSWORD': config('DB_PASSWORD'),
#            'HOST': config('DB_HOST'),
#            'PORT': '',
#        }
       
#    }
# # production
# else:
#    DATABASES = {
#        'default': dj_database_url.config(
#            default=config('DATABASE_URL')
#        )
#    }

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chatbot',
        'USER': 'mariga',
    'PASSWORD':'password',
    }
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'whatsappbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'whatsappbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chatbot',
        'USER': 'mariga',
    'PASSWORD':'password',
    }
}

 
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configure Django App for Heroku.
django_heroku.settings(locals())


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

WHATSAPP_URL = 'https://graph.facebook.com/v16.0/108118905582584/messages'
# WHATSAPP_TOKEN = 'Bearer EAASJmr0MOuwBACrkwkygfeT6FvaaRF7HBEqgMfuJZCVdbsTTyw5MZBnHgFhtxwUvbf2yASyIQZAUY32z9RY4ZA5gVLGGmGX5sKloBtAMJKOUfJcGOQ2SLqJG1TREbxo4ehFjR7KS9Oskr6x5b6khYPAy16m5pcjwKxqNl87IXwvnDMZCWAG59NtnVoUTPNy4PnOVGxbEtOgZDZD'
# WHATSAPP_TOKEN = 'EAASJmr0MOuwBACrkwkygfeT6FvaaRF7HBEqgMfuJZCVdbsTTyw5MZBnHgFhtxwUvbf2yASyIQZAUY32z9RY4ZA5gVLGGmGX5sKloBtAMJKOUfJcGOQ2SLqJG1TREbxo4ehFjR7KS9Oskr6x5b6khYPAy16m5pcjwKxqNl87IXwvnDMZCWAG59NtnVoUTPNy4PnOVGxbEtOgZDZD'

OPENAI_API_KEY = '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'