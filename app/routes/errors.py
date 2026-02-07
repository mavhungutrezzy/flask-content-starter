"""Error handlers."""

from flask import Blueprint, render_template

from app.seo.keywords import get_keywords
from app.seo.meta import get_meta
from app.seo.schemas import get_schema

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def not_found(error):
    """404 page."""
    seo = {
        "meta": get_meta("home"),
        "keywords": get_keywords("home"),
        "schema": get_schema("home"),
    }
    return render_template("errors/404.html", seo=seo), 404


@errors.app_errorhandler(500)
def server_error(error):
    """500 page."""
    seo = {
        "meta": get_meta("home"),
        "keywords": get_keywords("home"),
        "schema": get_schema("home"),
    }
    return render_template("errors/500.html", seo=seo), 500
