#!/bin/sh
source venv/bin/activate
exec gunicorn blog:app -b :8000 --name blogapp --log-level=debug --log-file=-
