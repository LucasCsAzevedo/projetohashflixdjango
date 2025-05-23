"""
Django settings for coxinhaflix project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
TOKEN_CSRF = os.getenv("TOKEN_CSRF")

if TOKEN_CSRF:
    SECRET_KEY = TOKEN_CSRF # Se estiver testando o online, vamos usar o token que criamos anteriormente
    CSRF_TRUSTED_ORIGINS = ['https://projetohashflixdjango-production-88c9.up.railway.app'] # Só aceitamos requisições de formulários caso esse venha desse link (Nosso site no momento)

else:
    SECRET_KEY = 'django-insecure-ot=t3jycb#7jyus$+-q+ls9q&h(+(erox-r&pg3n%tm$$vb)ic' # Caso contrátio, se estivermos no desktop usaremos esse token mesmo

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Vamos começar o deploy do site

ALLOWED_HOSTS = ['projetohashflixdjango-production-88c9.up.railway.app', 'localhost', '127.0.0.1'] # Lugar onde meu site vai rodar, no link e no localhost, tanto como nome, quanto como o código de IP


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filme',
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coxinhaflix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # Dentro do diretório 'base' posso criar uma , USAR QUANDO TODAS AS PÁGINAS SERÃO AFETADAS - ESQUELETO PADRÃO DO SITE (Header e Footer?)
        'APP_DIRS': True, # Crio uma pasta dentro do meu App e coloco os templates lá, USAR QUANDO QUISER ALTERAR SOMENTE UMA VIEW DE CADA APP
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'filme.context.lista_filmes_recentes',
                'filme.context.lista_filmes_populares',
            ],
        },
    },
]

WSGI_APPLICATION = 'coxinhaflix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

import dj_database_url

DATABASE_URL = 'postgresql://postgres:LaDXkaaXskaxGHSJyLGgsBZTMxabmjEE@shortline.proxy.rlwy.net:51130/railway'
if DATABASE_URL:
    DATABASES = {
        'default' : dj_database_url.config(default=DATABASE_URL, conn_max_age=1800)
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'filme.Usuario' # 'app.Classe'
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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/' # Topico 13

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [ # Topico 13
    BASE_DIR / 'static',
]

MEDIA_URL = 'media/' # Topico 13

MEDIA_ROOT = BASE_DIR / 'media' # Topico 13

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'filme:homefilmes'

LOGIN_URL = 'filme:login'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
