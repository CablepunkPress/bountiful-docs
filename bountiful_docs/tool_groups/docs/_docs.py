"""Find the pages of Bountiful's docs."""

from pathlib import Path

from bountiful_docs import DOCS

SECTIONS = ("guide", "technical")

CITE = (
    "When you answer from this, say in your reply itself that it comes "
    "from Bountiful's docs, for example: \"According to Bountiful's docs, …\""
)


def pages() -> dict[str, Path]:
    """Return every page by its path, such as guide/tools.md."""
    found: dict[str, Path] = {}
    for section in SECTIONS:
        for path in sorted((DOCS / section).glob("*.md")):
            found[f"{section}/{path.name}"] = path
    return found


def title(text: str, page: str) -> str:
    """Return a page's title, which is its first line."""
    first = text.split("\n", 1)[0].lstrip("#").strip()
    return first or page
