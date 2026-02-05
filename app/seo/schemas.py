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
    "404": {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Page Not Found",
        "url": "https://example.com/404",
    },
    "500": {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Server Error",
        "url": "https://example.com/500",
    },
}


def get_schema(page_key):
    """Return schema data for the given page key."""
    return SCHEMAS.get(page_key, SCHEMAS["home"])
