"""Basic email-address validation without external dependencies."""
from __future__ import annotations


def validate_email(address: str) -> bool:
    """Return whether *address* has a plausible email-address shape."""
    if not isinstance(address, str) or len(address) > 254:
        return False
    if any(character.isspace() for character in address):
        return False
    if address.count("@") != 1:
        return False

    local_part, domain = address.split("@")
    if not local_part or not domain:
        return False
    if local_part.startswith(".") or local_part.endswith("."):
        return False
    if ".." in local_part or ".." in domain:
        return False
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return True
