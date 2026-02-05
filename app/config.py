"""Configuration settings for different environments."""

import os


class BaseConfig:
    """Base configuration with performance-focused defaults."""

    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    TEMPLATES_AUTO_RELOAD = False

    # Compression settings (gzip + brotli where supported).
    COMPRESS_ALGORITHM = ["br", "gzip"]
    COMPRESS_MIN_SIZE = 512

    # Cache HTML pages for at least 1 hour.
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 3600


class DevelopmentConfig(BaseConfig):
    """Development-friendly config."""

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(BaseConfig):
    """Production config with debug disabled."""

    DEBUG = False


def get_config():
    """Select configuration based on APP_ENV (development/production)."""
    env = os.getenv("APP_ENV", "production").lower()
    if env == "development":
        return DevelopmentConfig
    return ProductionConfig
