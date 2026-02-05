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
    "404": {
        "title": "Page Not Found | Content Platform Starter",
        "description": "The page you requested could not be found. Explore our latest content and resources.",
    },
    "500": {
        "title": "Server Error | Content Platform Starter",
        "description": "We hit a snag. Please try again soon while we resolve the issue.",
    },
}


def get_meta(page_key):
    """Return meta data for the given page key."""
    return META.get(page_key, META["home"])
