# The agent folder

An agent is a folder in the home folder, named by its ID, such as `~/alice`. Everything that is the agent's own is in it:

```
~/alice/
    agent.json      who the agent is, and the tool groups it has added
    persona.md      its personality
    context/        notes it keeps in mind
    data/           its memory and its logs
    .gitignore      keeps data/ out of git
    config.toml     changes to its settings, only if you make one
```

## Where the files come from

`bountiful create` writes `agent.json` and copies the rest from basic-bot's templates, in `basic_bot/templates/agent/`. The templates are copied only once, when the agent is made. After that the files are yours, and new versions of Bountiful never overwrite them.

`data/` is made the first time the agent starts. `config.toml` is only there if you make one.

## agent.json

`agent.json` says who the agent is:

```json
{
    "id": "alice",
    "name": "Alice",
    "description": "A Bountiful agent",
    "tools": {
        "wikipedia": {}
    }
}
```

- **`id`** never changes. It names the folder, the database, and the agent's keys in the keyring.
- **`name`** is what the agent is called. You can change it by hand.
- **`description`** is a line about the agent.
- **`tools`** lists the plugin tool groups the agent has added, each with its settings. `bountiful add` and `bountiful remove` write this part. It's left out when the agent has no plugins.

## persona.md

The persona is the first part of the agent's prompt. Where it says `{{ name }}`, the agent's name is automatically added from its `agent.json`. A new agent's persona is short: its name and a line about its personality. What every agent needs to know, such as what it is and how to use its memory and tools, is in [the instructions](instructions.md), so rewriting the persona never removes it. You can rewrite the agent's persona however you like. Keep it to personality: a small model can follow a rule such as "point out every inconsistency" too eagerly, and argue with you over nothing. Changes take effect the next time you start the agent.

## context/

Every Markdown file in `context/` is added to the prompt, under a `# CONTEXT` heading, every turn. The files go in alphabetical order. Files whose names start with an underscore, such as `_README.md`, are skipped, so you can keep notes there that the agent never sees. Use this folder for material you wish the agent to have but that you do not consider part of its personality. For example, this would be a place to add information about yourself and your preferences. Changes take effect the next time you start the agent.

## config.toml

`config.toml` changes the agent's settings. Each setting is a name and a value:

```toml
log_reasoning = true
max_tool_rounds = 10
```

The settings and their defaults are listed in basic-bot's `basic_bot/config.py` and basic-ui's `basic_ui/config.py`. A name in `config.toml` replaces the setting of the same name, whatever its capitals. A few that matter most:

| Setting | Default | What it does |
| --- | --- | --- |
| `max_tool_rounds` | `8` | How many rounds of tool calls one turn may make before the agent must answer. |
| `log_reasoning` | `false` | Writes the model's reasoning to the agent's log. |
| `flask_port` | `11777` | The port of the web page. |
| `chat_port`, `summary_port`, `embedding_port` | `11555`, `11444`, `11333` | The ports of the three model servers. |

The file is read once, when the agent starts.

## data/

`data/` is the agent's memory and its logs:

```
data/
    alice.db                the conversations and the summary
    logs/agent/alice.log    what the agent did
    logs/server/            what the model servers did
    slots/                  the chat server's saved cache
```

- **The database**, `ID.db`, is a SQLite file. It holds every message, the summary, and what's needed to search them.
- **The agent log** records each session's start and end, settings changes, tool calls, folds, and how long each request took. It's rotated, so it never grows past a fixed size.
- **The server logs** have one file for each time a model server ran. The newest 20 of each kind are kept.
- **The slots** hold the chat server's cache, saved when it stops and loaded when it starts again, so the conversation doesn't have to be read again from the start.

`.gitignore` keeps `data/` out of git, so if you keep the agent's folder in git, its memory can't be pushed anywhere by accident.
