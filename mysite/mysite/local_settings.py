import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MY_SECRET_KEY = '$1lhn_#-kv4j7#fcvk+%bg(7(6z*+^e^1^i+1ml$x=74t_w@@8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True