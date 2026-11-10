"""List the pages of Bountiful's docs."""

import json

import _docs

TOOL = {
    "name": "list_docs",
    "description": (
        "List the pages of Bountiful's documentation, with each page's path "
        "and title. Bountiful is the software you run on. Use this when the "
        "user asks about Bountiful or how you work, such as installing, "
        "agents, tools, memory, or models. Then read the page that fits "
        "with read_doc."
    ),
    "input_schema": {"type": "object", "properties": {}},
}


def handler(context: dict, **_) -> str:
    """Return the path and title of every page."""
    listed = [
        {"page": page, "title": _docs.title(path.read_text(), page)}
        for page, path in _docs.pages().items()
    ]
    return json.dumps({
        "pages": listed,
        "note": (
            "Pages in guide/ explain how to use Bountiful. Pages in "
            "technical/ explain how each part works. Read one with read_doc."
        ),
    })
