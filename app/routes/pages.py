"""Public page routes."""

from flask import Blueprint, render_template

from app.seo.keywords import get_keywords
from app.seo.meta import get_meta
from app.seo.schemas import get_schema
from app.utils.cache import cache

pages = Blueprint("pages", __name__)


@pages.route("/", endpoint="index")
@cache.cached(timeout=3600)
def home():
    """Home page."""
    seo = {
        "meta": get_meta("home"),
        "keywords": get_keywords("home"),
        "schema": get_schema("home"),
    }
    return render_template("pages/home.html", seo=seo)


@pages.route("/about")
@cache.cached(timeout=3600)
def about():
    """About page."""
    seo = {
        "meta": get_meta("about"),
        "keywords": get_keywords("about"),
        "schema": get_schema("about"),
    }
    return render_template("pages/about.html", seo=seo)
