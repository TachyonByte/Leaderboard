#!/bin/bash
# Collect static files
cd ctf
python manage.py collectstatic --noinput
python manage.py migrate

# Start Daphne
daphne -b 0.0.0.0 -p 8089 ctf.asgi:application

# Start Nginx (assuming it's configured to serve static files)
nginx -g "daemon off;"