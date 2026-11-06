# The web page

The web page is basic-ui. It's a small web server, made with Flask, that runs on your own computer. It shows the conversation and sends your messages to the agent through the session.

## How it starts

`bountiful ID` calls basic-ui's `launch`, in `basic_ui/launch.py`. It:

1. opens the agent's session,
2. starts the chat model,
3. serves the page at `http://localhost:11777` until you press Control-C.

The server listens only on `127.0.0.1`, so the page can only be opened on your own computer. The port is the `flask_port` setting, and the address is `host`.

## How it's built

- **Flask** answers each request from the browser.
- **Jinja templates**, in `basic_ui/templates/`, are the HTML. `index.html` is the page, and the files in `partials/` are the pieces that get added to it.
- **HTMX**, in `static/js/htmx.js`, sends a request when you press Send, and puts the HTML that comes back into the page. The page never reloads.
- **`static/css/styles.css`** is how the page looks.

The browser keeps nothing of its own. The session holds the conversation and the settings, and every request gets back the HTML to show.

## When the page opens

The page shows the last 10 messages, with a line saying which ones they are, such as `Last 10 messages loaded: #91–#100`. A new agent shows `No messages yet.` The number is the `history_limit` setting.

## A message, in three steps

Each message goes through three requests, so each step shows as soon as it's ready:

| Request | What it does | What you see |
| --- | --- | --- |
| `POST /message` | Shows your message straight away. | Your message, and "Thinking…" |
| `POST /reply` | Asks the session for the reply. | The reply, in place of "Thinking…" |
| `POST /memory` | Runs a fold, only when the reply says one is due. | "Updating memory…", then "Memory updated." |

The message box stays greyed out until the last step is done. Each response says whether to turn it back on, so the server decides when you can send the next message.

If something goes wrong, the error shows in the conversation as a message of its own, and the message box turns back on. The terminal shows the details.

## Replies

The agent's replies are written in Markdown. basic-ui turns them into HTML with markdown-it-py, which handles headings, lists, tables, and links. Links open in a new tab.

Under each reply is a line saying what wrote it:

```
Gemma 4 26B A4B QAT UD-Q4_K_XL · Deep Reasoning
```

## Keeping the page safe

A reply is written by a model, so the page treats it as untrusted:

- The agent’s Markdown, such as headings, lists, and links, becomes HTML. Any HTML the agent writes itself is shown as plain text, so it can never become part of the page..
- Unsafe links, such as `javascript:` links, are refused.
- The page loads nothing from anywhere else on the internet. Every file it uses comes from basic-ui itself.
- The page runs no scripts but its own, can't be put inside another website's page, and only sends requests back to its own server.
