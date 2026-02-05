"""Cache extension setup."""

from flask_caching import Cache

# Simple in-memory cache keeps infra costs low and is safe for static content.
cache = Cache()
