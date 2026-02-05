"""Keyword sets for SEO."""

KEYWORDS = {
    "home": [
        "flask boilerplate",
        "seo optimized",
        "fast content site",
        "python 3.12",
        "bootstrap 5",
    ],
    "about": [
        "flask content platform",
        "caching",
        "gzip brotli",
        "seo architecture",
    ],
    "404": [
        "page not found",
        "content platform",
        "seo site",
        "flask starter",
    ],
    "500": [
        "server error",
        "content platform",
        "flask uptime",
        "seo performance",
    ],
}


def get_keywords(page_key):
    """Return keywords for the given page key."""
    return KEYWORDS.get(page_key, KEYWORDS["home"])
