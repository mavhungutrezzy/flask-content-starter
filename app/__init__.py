"""Flask application factory and global app setup."""

from flask import Flask, request
from flask_compress import Compress

from app.config import get_config
from app.routes.errors import errors
from app.routes.pages import pages
from app.routes.seo import seo_bp
from app.seo.keywords import get_keywords
from app.seo.meta import get_meta
from app.seo.schemas import get_schema
from app.sitemap import sitemap
from app.utils.cache import cache


compress = Compress()


def create_app():
    """Application factory for creating the Flask app."""
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(get_config())

    # Initialize extensions.
    cache.init_app(app)
    compress.init_app(app)
    sitemap.init_app(app)

    # Register blueprints.
    app.register_blueprint(pages)
    app.register_blueprint(errors)
    app.register_blueprint(seo_bp)

    @app.context_processor
    def inject_seo():
        """Inject default SEO data into all templates."""
        return {
            "seo": {
                "meta": get_meta("home"),
                "keywords": get_keywords("home"),
                "schema": get_schema("home"),
            }
        }

    @app.after_request
    def add_cache_headers(response):
        """Add long-term cache headers for static assets.

        Static assets are versioned by their filenames, so we can cache them for a year
        to reduce bandwidth and improve repeat-visit performance.
        """
        if request.path.startswith("/static/"):
            response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
        return response

    return app
