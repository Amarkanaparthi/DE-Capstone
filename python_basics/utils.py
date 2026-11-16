def clean_name(name: str) -> str:
    """Trim spaces, collapse repeated spaces, and capitalise each word."""
    return " ".join(name.split()).title() if name else ""

def parse_amount(value: str) -> float:
    """Turn text like '₹ 1,234.50' into 1234.5. Raise ValueError if there are no digits."""
    text = value.strip()
    negative = text.startswith("-")
    cleaned = "".join(ch for ch in text if ch.isdigit() or ch == ".")
    if not any(ch.isdigit() for ch in cleaned):
        raise ValueError(f"Cannot parse amount: {value!r}")
    amount = float(cleaned)
    return -amount if negative else amount

def summarize(numbers: list[float]) -> dict[str, float]:
    """Return min, max and avg of numbers. Return {} for an empty list."""
    if not numbers:
        return {}
    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": sum(numbers) / len(numbers)
    }