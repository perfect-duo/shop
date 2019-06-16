"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "apps/users/dysms_python"))
sys.path.insert(0, os.path.join(BASE_DIR, "alipay-master"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ote401b5xp!yj)j^@3@d+#ktf1p!67j4hoqhk@a5$ftd46d56y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'goods',
    'trade',
    'user_operation',
    'xadmin',
    'crispy_forms',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'
AUTH_USER_MODEL = 'users.UserProfile'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/setti ngs/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "wang_shop",
        'HOST': "127.0.0.1",
        "USER": "root",
        "PASSWORD": "123456",
        "PORT": "3306",
    }
}
AUTHENTICATION_BACKENDS = (
    'users.views.CustomsBackends',
    "social_core.backends.weibo.WeiboOAuth2"
)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
REST_FRAMEWORK = {
    "PAGE_SIZE": 10,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    #  对于相应的api进行限速
    'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ),
    'DEFAULT_THROTTLE_RATES': {
            'anon': '100/day',
            'user': '10/minutes'
        }
}


# 手机号码正则表达式
VERIFY_MOBILE = "^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$"
# 短信验证码签名
MESSAGE_SIGNATURE = "多多网"
TEMPLATE_CODE = "SMS_148613194"

# 支付宝公钥， 私钥
ALIPAY_PUBLIC = os.path.join(BASE_DIR, "alipay-master/alipay/key/public.txt")
ALIPAY_PRIVATE = os.path.join(BASE_DIR, "alipay-master/alipay/key/private.txt")

# 设置缓存
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 5

}
# 微博登录跳转地址
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/goods/goods/'

# 设置微博app_key 和secret
SOCIAL_AUTH_WEIBO_KEY = "*"
SOCIAL_AUTH_WEIBO_SECRET = "*****"

EMAIL_HOST = 'smtp.139.com'
EMAIL_POST = 25
EMAIL_HOST_USER = '15836572803@139.com'
EMAIL_HOST_PASSWORD = '***'
EMAIL_USE_TLS = True
EMAIL_FROM = EMAIL_HOST_USER
