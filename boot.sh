#!/bin/sh
source venv/bin/activate
exec gunicorn -b :5000 blog:app
exec venv/bin/python dummy_entry.py