# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7#!h-t6*yko=i)pp$w#m8)h32edsa#8obibh=fzvuy897z4phd'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cofe',
        'USER': 'cofe',
        'PASSWORD': 'cofe',
        'HOST': '127.0.0.1',
    }
}