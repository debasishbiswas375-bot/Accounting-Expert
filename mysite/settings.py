import os
from pathlib import Path

# BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY
SECRET_KEY = os.environ.get("SECRET_KEY", "postgresql://neondb_owner:npg_RVfsPe3aAL7c@ep-little-scene-a1znmqcr-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

# DEBUG mode (set to False in production)
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["accountingexpert.onrender.com"]


# Application definition
INSTALLED_APPS = [
    'converter',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'your_project_name.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'your_project_name.wsgi.application'

# Database (use Render Postgres or SQLite for testing)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME", "mydb"),
        'USER': os.environ.get("DB_USER", "user"),
        'PASSWORD': os.environ.get("DB_PASSWORD", "password"),
        'HOST': os.environ.get("DB_HOST", "localhost"),
        'PORT': os.environ.get("DB_PORT", "5432"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Superuser creation using environment variables (optional)
# Run `python manage.py createsuperuser` manually if needed
DJANGO_SUPERUSER_USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
DJANGO_SUPERUSER_PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")
DJANGO_SUPERUSER_EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
