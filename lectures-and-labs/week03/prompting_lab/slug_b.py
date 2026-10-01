import re
import unicodedata


def slugify(title: str) -> str:
    """Convert a title to a lowercase, hyphen-separated slug."""
    normalized = (
        title.lower()
        .replace("ß", "ss")
        .replace("'", "")
        .replace("‘", "")
        .replace("’", "")
    )
    normalized = unicodedata.normalize("NFKD", normalized)
    ascii_title = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_title).strip("-")
    return slug if slug else title
