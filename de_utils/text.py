def clean_name(name: str) -> str:
    """Trim spaces, collapse repeated spaces, and capitalise each word."""
    return " ".join(name.split()).title() if name else ""