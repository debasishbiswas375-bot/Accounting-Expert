#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies (ensure "pip" is the first word)
pip install -r requirements.txt

# Prepare the site
python manage.py collectstatic --no-input
python manage.py migrate

# Create Admin (Change password below)
export DJANGO_SUPERUSER_PASSWORD="admin123"
python manage.py createsuperuser --noinput --username admin --email admin@example.com || true
