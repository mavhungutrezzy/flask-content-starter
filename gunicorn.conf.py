"""Gunicorn configuration for production."""

bind = "0.0.0.0:8000"
workers = 2
threads = 4
timeout = 30

# Preload app to reduce startup time per worker.
preload_app = True
