"""SEO route handlers."""

from flask import Blueprint, current_app

seo_bp = Blueprint("seo", __name__)


@seo_bp.route("/ads.txt")
def ads_txt():
    """Serve ads.txt for AdSense compliance."""
    return current_app.send_static_file("ads.txt")


@seo_bp.route("/robots.txt")
def robots_txt():
    """Serve robots.txt. from static"""
    return current_app.send_static_file("robots.txt")
