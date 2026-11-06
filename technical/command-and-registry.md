# The bountiful command and the registry

## Where the command lives

The command's code is `bountiful/command.py`, in the bountiful repository. bountiful's `pyproject.toml` declares it as a console script, so when the setup installs bountiful into the venv, pip makes the command `.venv/bin/bountiful`. That command always runs with the venv's Python, from any folder. The setup then links `~/.local/bin/bountiful` to it.

The hub uses every other part, so the command calls basic-bot, basic-ui, and extend-a-bot directly to do its work.

## How it reads what you type

The first word after `bountiful` is either a subcommand, such as `create`, or an agent's ID, such as `alice`. Subcommands are checked first. That's why no agent's ID can be a subcommand.

`bountiful` by itself, or `bountiful help`, prints the usage.

If the first word is neither a subcommand nor a registered ID, the command says so and stops.

## The subcommands

| Subcommand | What it does | Where the work is done |
| --- | --- | --- |
| `create NAME` | Makes an agent's folder and registers it. | basic-bot |
| `ID` | Starts the agent and its web page. | basic-ui and basic-bot |
| `agents` | Lists the registered agents. | basic-bot's registry |
| `register ID` | Adds an existing agent's folder to the registry. | basic-bot's registry |
| `forget ID` | Takes an agent off the registry. Its folder is left alone. | basic-bot's registry |
| `tools`, `tools ID` | Lists the tool groups, or one agent's. | extend-a-bot |
| `add GROUP ID` | Adds a tool group to an agent, and asks for any keys. | extend-a-bot |
| `remove GROUP ID` | Removes a tool group, with its settings and keys. | extend-a-bot |
| `version` | Prints the installed version. | bountiful |
| `update` | Installs the newest release. | bountiful |

Two more subcommands work but aren't in the usage for now:

- `chat ID` runs an agent in the terminal instead of the web page.
- `models` chooses optional chat models to download or remove.

## Creating an agent

`bountiful create NAME` makes the ID from the name. If the ID is taken, it tries `ID-1`, then `ID-2`, and so on. An ID counts as taken if it's registered, if it's a subcommand or a reserved word, or if something in the home folder already has that name, in any mix of capitals and small letters.

It asks before it makes anything, so it only runs in a terminal. Then basic-bot makes the folder `~/ID`, writes `agent.json`, and copies in the template files. Last, the ID is registered.

## Updating

`bountiful update` only follows the `stable` branch. New releases are tags, and `stable` is only ever moved to the newest one. So updating means moving the clone to wherever `stable` is now on GitHub.

It checks, in order, that:

1. the clone is a git clone,
2. it's on `stable`,
3. it has no changes of its own,
4. GitHub can be reached.

If the clone is already where `stable` is, there's nothing to do. Otherwise it prints the new release's tag and its notes, which are the tag's message, and asks. Then it runs `git pull`, and runs `python3 build.py` to rebuild.

## The registry

The registry is Bountiful's list of agents, kept in `~/.bountiful/agents.json`. It holds only IDs:

```json
{
  "agents": [
    "alice",
    "gretel"
  ]
}
```

It doesn't need to record where each agent's folder is, because the folder always follows from the ID: agent `alice` is always in `~/alice`. The ID, the folder's name, and the name of the agent's database are the same word.

**Registering** an ID makes it something `bountiful ID` can start. Before it registers an ID, basic-bot checks that `~/ID` exists, holds an `agent.json`, and that the ID in that file is this ID.

**Forgetting** an ID only takes it off the list. Nothing in the agent's folder is touched.

The list is always written whole, through a temporary file, so a crash can never leave it half written.
