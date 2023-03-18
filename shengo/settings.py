from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n)m$%*iz3(cler1vt)w2e0xbxay%6#7s!a=!8xv^4h(75r+zri'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',  
    'crispy_forms',
    'crispy_bootstrap4',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'dashboard',
    'setting',
    'sales',
    'gifts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
]

ROOT_URLCONF = 'shengo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django_auto_logout.context_processors.auto_logout_client',
            ],
        },
    },
]

WSGI_APPLICATION = 'shengo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # to access the media from our pc on browser
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'


#Reset password using email confirmation
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'habtamuasayto360@gmail.com'
EMAIL_HOST_PASSWORD = 'pzfatkiufthvhine' # this password is generated on my gmail


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)


#Locale
from django.utils.translation import gettext_lazy as _ 
import django.conf.locale
EXTRA_LANG_INFO = {
    'am': {
        'bidi': False,
        'code': 'am',
        'name': 'Amharic',
        'name_local': 'አማርኛ',
    },
    'en': {
        'bidi': False,
        'code': 'en',
        'name': 'English',
        'name_local': 'English',
    },
}
d = django.conf.locale.LANG_INFO.copy()
d.update(EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = d


LANGUAGE_CODE = 'am'

LANGUAGES = [
    ('en', _('English')),
    ('am', _('Amharic')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


#Logout based on session 
AUTO_LOGOUT = {'IDLE_TIME':2000,
               'SESSION_TIME': 3600,
               'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
               'MESSAGE': 'The session has expired. Please login again to continue.',
               }  # logout after 10 minutes of downtime