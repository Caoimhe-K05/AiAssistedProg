"""Minimal email-address validation."""
from __future__ import annotations


def validate_email(address: str) -> bool:
    """Return whether *address* has an @ and a dot after it within 254 chars."""
    if len(address) > 254 or "@" not in address:
        return False

    return "." in address.split("@", 1)[1]
