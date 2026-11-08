# Tools

A tool is plain Python. The chat model never runs a tool itself. It writes a tool call, the tool's name and its inputs, such as `recall_message(seq=107)`. basic-bot runs the tool's Python and gives the result back to the model to read. [The prompt](prompt.md) explains how tools reach the model and what happens during a turn.

## The three kinds

| Kind | Also called | Where it lives | Who has it |
| --- | --- | --- | --- |
| Default tools | the tool belt | basic-bot's memory group, `basic_bot/tool_groups/memory/` | every agent |
| Plugin tools | the tool box | an installed package, such as extend-a-bot's `tool_box/` | agents that have added them |
| Custom tools | the tool shed | the agent's own `tools/` folder | that agent, once it has added them |

The default tools are the memory group, `search_archive` and `recall_message`, explained in [Memory](memory.md). Like every group, it's a folder with a `tool.json`.

basic-bot runs every tool, but only the default tools belong to it. It never names a plugin or a custom group (such as wikipedia or google) in its code. A package offers plugin tools by plugging into basic-bot's tools jack: extend-a-bot's `pyproject.toml` declares its `tool_box/` folder under the `basic_bot.tool_box` entry point, and basic-bot finds it there.

## Tool groups

Plugin and custom tools come in groups. A group is a folder:

```
wikipedia/
    tool.json             the group's name, description, and what it needs
    search_wikipedia.py   one tool
    read_wikipedia.py     another tool
    _wiki.py              code the group's tools share
    settings.toml         the settings an agent starts with
    instructions.md       how to use the group, for the system prompt
```

**`tool.json`** describes the group for people. `bountiful tools` and `bountiful add` show it:

```json
{
    "name": "brave",
    "description": "Search the web with Brave Search, for news, recent events, and subjects Wikipedia doesn't cover",
    "sends": "What the agent searches for goes to Brave Search (search.brave.com), under your Brave Search API key. ...",
    "keys": [
        {"name": "api_key", "label": "Brave Search API key"}
    ]
}
```

- **`sends`** says what leaves your computer when the tools are used. `bountiful add` shows it before it adds the group.
- **`keys`** lists the secrets the group needs. `bountiful add` asks for each one.
- **`dependencies`**, in a custom group, lists Python packages the group needs. The setup installs them.

**Each tool** is a `.py` file with two things in it:

- **`TOOL`**, a dictionary with the tool's `name`, its `description`, and its inputs, `input_schema`. This is what the model sees.
- **`handler`**, the Python function that does the work and returns the result.

**Files starting with an underscore**, such as `_wiki.py`, aren't tools. They hold code the group's tools share.

**`instructions.md`** goes into the system prompt of every agent that has the group.

## Adding a group to an agent

A plugin or custom group only loads for an agent that has added it. `bountiful add GROUP ID` adds it:

1. It shows what the group sends.
2. It asks for each key, and stores it in the keyring.
3. It copies the group's `settings.toml` into the `tools` section of the agent's `agent.json`.

The agent's settings for the group live in `agent.json` from then on, where you can change them. `bountiful remove GROUP ID` removes the group's settings and deletes its keys.

A custom group with the same name as a plugin group takes the plugin's place for that agent.

## Settings and keys

When a tool runs, its handler is given the agent's ID and the agent's settings for its group. So one group, installed once, serves every agent, each with its own settings.

A tool's description can name a setting in double braces, such as `{{ language }}`. basic-bot fills it in from the agent's settings when the tools load.

Keys are kept in the keyring, never in the agent's folder. Each key is stored under the agent's ID and named by its group, such as `brave.api_key`, so two agents never share a key. A tool reads its key when it runs.

## The record of each turn

basic-bot keeps a record of every tool call in a turn, saved with the agent's reply in the `tools` column of the `messages` table. Each call's record holds:

- **`tool`**, the tool's name,
- **`input`**, what the model asked for,
- **`outcome`**: `ok`, `error`, `nothing found`, or `refused` past the round limit,
- **`sources`**, the pages the result came from.

A tool names its sources with a `sources` list in its result. basic-bot moves them into the record and takes them out of the result before the model reads it. The reply's annotation shows the record on later turns, so the model knows which of its past answers came from a lookup.

The Wikipedia and Brave results also end with a `cite` line, which tells the model to name its source in its reply.
