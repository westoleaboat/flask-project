#!/bin/sh

flask db upgrade

# flask deploy

exec gunicorn --bind 0.0.0.0:80 "app:create_app()"