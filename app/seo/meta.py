"""SEO meta titles and descriptions."""

META = {
    "home": {
        "title": "Content Platform Starter | Fast, SEO-Friendly Flask",
        "description": "A production-ready Flask boilerplate optimized for SEO, speed, and low server cost.",
    },
    "about": {
        "title": "About | Content Platform Starter",
        "description": "Learn how this Flask starter keeps content pages fast, cacheable, and search-friendly.",
    },
}


def get_meta(page_key):
    """Return meta data for the given page key."""
    return META.get(page_key, META["home"])
