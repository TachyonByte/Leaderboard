#!/bin/bash

# Set environment variables
export DJANGO_SETTINGS_MODULE=ctf.settings

# Collect static files
python ctf/manage.py collectstatic --noinput

# Start Daphne
daphne -b 0.0.0.0:8089 ctf/ctf.asgi:application

# Start Nginx (assuming it's configured to serve static files)
nginx -g "daemon off;"