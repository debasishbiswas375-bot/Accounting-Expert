#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Recreate the missing tables (Fixes: "relation auth_user does not exist")
python manage.py migrate

# Create the admin account automatically
# It uses environment variables so you don't expose your password in code
if [[ $CREATE_SUPERUSER ]]; then
  python manage.py createsuperuser --noinput || true
fi
