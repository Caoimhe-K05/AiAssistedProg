"""Basic email-address validation."""
from __future__ import annotations

import re


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_email(address: str) -> bool:
    """Return whether *address* has a basic email-address shape."""
    return bool(EMAIL_PATTERN.fullmatch(address))
