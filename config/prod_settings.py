from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# желательно изменить эту строку на любую рандомню 50 символов
SECRET_KEY = 'ld*bz_k9xwy3+c**xb#k2qna48r2(k2ed9wgq3orwgxvut!wyv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# тута звездочку сменить на днсимя сайта
ALLOWED_HOSTS = ['*']
# туточки поменять настройки бд
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbname',
        'USER': 'db_username',
        'PASSWORD': 'ad_userpassword',
        'HOST': 'ip_server_db',
        'PORT': 'port_to_db',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SMTP yandex server
DEFAULT_FROM_EMAIL = 'tonermaster.service@yandex.by'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_HOST_USER = "tonermaster.service@yandex.by"
EMAIL_HOST_PASSWORD = "ldfnthvjcfxfxb"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
