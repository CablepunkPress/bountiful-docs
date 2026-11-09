# The session

A session is a running agent, from the moment you start it to the moment you stop it. It's the one way a front end, such as the web page, talks to the agent. A front end never touches the models, the database, or the servers itself. It asks the session.

The session is in basic-bot's `basic_bot/session.py`. The `bountiful` command opens it and hands it to the front end: basic-ui's web page for `bountiful ID`, and the terminal for `bountiful chat ID`. Both show the same agent, because both go through the session.

## What a front end does with it

A front end uses a session in this order:

```python
with Session.open(agent_path, data_dir) as session:
    session.start()
    reply = session.send("Hello")
    if reply.memory_update_due:
        session.update_memory()
```

- **`Session.open`** gets the agent ready. It reads `agent.json` and `config.toml`, starts the agent's log, and builds the runtime. Nothing is running yet.
- **`start`** starts the chat model's server.
- **`send`** answers a message. It returns the reply as soon as the reply is written and the turn is saved.
- **`update_memory`** runs a fold. A front end calls it when a reply says one is due, and shows "Updating memory…" while it runs.
- **`close`** stops every server the session started. The `with` block calls it when the front end stops, however it stops.

A front end can also ask for the recent messages with **`history`**, and for the settings to show with **`controls`**. It changes those settings with **`select_model`**, **`set_reasoning`**, and **`set_effort`**.

## One thing at a time

A session does one thing at a time. If a front end sends a message while the agent is still answering, or still updating its memory, the session says it's busy.

## Memory is always up to date

When a reply says a fold is due, the front end should call `update_memory`. If it doesn't, or the fold is interrupted, the next `send` runs the fold first. So a message is never answered with memory out of date.

A fold that fails doesn't lose anything. The turn was already saved, and the fold runs again before the next message is answered.

## Times

The session stamps each message with its own time: yours when it arrives, the agent's when its reply is finished. Times are stored in UTC. A front end shows them in your local time.

## Warming

After each reply, after each fold, after a setting changes, and when the session starts, the session warms the chat server. It sends the conversation to the server ahead of time, as the next message will find it. Then, when you send the next message, the server only has to read your new message.

Warming runs in the background, so you can send a message right away. If you do, the message waits for the warming to finish, and nothing is lost.

## Stopping

Control-C, closing the terminal window, logging out, and an ordinary `kill` all end in `close`, so the model servers are stopped. If the program is forced to quit, each server has a watchdog, a small program that stops its server when the program that started it is gone.

## The runtime

Underneath the session is the runtime, in `basic_bot/runtime.py`. The runtime is everything that makes this agent this agent while it runs: its ID and folder, its prompt's persona and context, its tools, its database, and the providers for its three models. `Session.open` builds it once, in `basic_bot/factory.py`, and the session passes it to everything that does the work.

The session is what a front end sees. The runtime is what the session works with.
