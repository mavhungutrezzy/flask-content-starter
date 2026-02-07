"""Sitemap configuration and generators."""

from datetime import date

from flask_sitemap import Sitemap

sitemap = Sitemap()


@sitemap.register_generator
def sitemap_pages():
    """Register all pages in sitemap with metadata."""
    today = date.today()

    # Homepage with highest priority
    yield "pages.index", {}, today, "weekly", 1.0

    # Other pages
    yield "pages.about", {}, today, "monthly", 0.8
