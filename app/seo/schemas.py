"""JSON-LD structured data for pages."""

SCHEMAS = {
    "home": {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Content Platform Starter",
        "url": "https://example.com",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://example.com/search?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    },
    "about": {
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "name": "About Content Platform Starter",
        "url": "https://example.com/about",
    },
}


def get_schema(page_key):
    """Return schema data for the given page key."""
    return SCHEMAS.get(page_key, SCHEMAS["home"])
