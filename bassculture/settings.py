"""
Django settings for bassculture project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r*v$obtdmh1dsk82#9*@k=6#+a#-^8!h#fke=d^om#u6v@s%4#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bassculture',
    'django_extensions',
    'rest_framework',
#    'static_precompiler',
#    'mod_wsgi.server',
    'bootstrap3',
    'clear_cache',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.middleware.security.SecurityMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'bassculture.urls'

WSGI_APPLICATION = 'bassculture.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bassculture',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
#    'static_precompiler.finders.StaticPrecompilerFinder',
)

#SESSION_COOKIE_SECURE = True

#SECURE_CONTENT_TYPE_NOSNIFF = True

#CSRF_COOKIE_SECURE = True

#CSRF_COOKIE_HTTPONLY = True

#SECURE_HSTS_SECONDS = '0'

#SECURE_HSTS_INCLUDE_SUBDOMAINS = True

#ALLOWED_HOSTS = '*'

#SECURE_BROWSER_XSS_FILTER = True

#SECURE_SSL_REDIRECT = True

#X_FRAME_OPTIONS = 'DENY'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BOOTSTRAP3 = {
    
    'include_jquery': True,
    'jquery_url': 'http://code.jquery.com/jquery-1.11.3.min.js'

}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = (os.path.join(PROJECT_DIR, 'static'))
STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

SOLR_SERVER = 'http://localhost:8080'
