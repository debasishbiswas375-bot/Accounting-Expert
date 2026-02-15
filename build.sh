#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files for the admin panel
python manage.py collectstatic --no-input

# 3. Run database migrations to Neon
python manage.py migrate

# 4. Create your Admin user (Change the password below!)
export DJANGO_SUPERUSER_PASSWORD="YourSecurePassword123"
python manage.py createsuperuser --noinput --username admin --email admin@example.com || true
