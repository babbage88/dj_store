#!/usr/bin/env bash
source .venv/bin/activate
gunicorn store_mg.wsgi:application --bind 0.0.0.0:8000 --workers 4
