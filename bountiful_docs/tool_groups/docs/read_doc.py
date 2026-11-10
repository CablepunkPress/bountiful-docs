"""Read one page of Bountiful's docs."""

import json

import _docs

TOOL = {
    "name": "read_doc",
    "description": (
        "Read one page of Bountiful's documentation, whole, by its path "
        "from list_docs, such as guide/tools.md."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "page": {
                "type": "string",
                "description": "The page's path, as list_docs gave it",
            },
        },
        "required": ["page"],
    },
}


def handler(context: dict, page: str = "", **_) -> str:
    """Return a page's text, with its source and the cite line."""
    wanted = str(page).strip().lstrip("/")
    path = _docs.pages().get(wanted)
    if path is None:
        return json.dumps({
            "error": f"No page is named '{page}'. Call list_docs for the pages.",
        })
    text = path.read_text()
    return json.dumps({
        "page": wanted,
        "title": _docs.title(text, wanted),
        "source": f"Bountiful's docs, {wanted}",
        "text": text,
        "cite": _docs.CITE,
    })
