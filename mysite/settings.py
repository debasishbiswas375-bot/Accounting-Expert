import os
import dj_database_url # Make sure this is in your requirements.txt

# ... (Keep your existing SECRET_KEY and INSTALLED_APPS) ...

DEBUG = False
ALLOWED_HOSTS = ['*'] # Or your specific .onrender.com domain

# Database connection to Neon
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Static files (required for Render)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
