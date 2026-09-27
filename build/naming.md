# Naming

The first time a user runs `python build.py`, the script names the agent. Naming happens once. On every later run, build.py sees that the agent already has a name and skips straight to building the environment.

## How it works

The template's `dashboard.json` ships with the id `my-agent`, which acts as a sentinel. When build.py finds that value, it knows this is a first run. It takes the name of the directory the user cloned into, lowercases it, and proposes it as the agent's id. It derives a display name from the same word by turning hyphens and underscores into spaces and capitalizing each word, so a directory named `alice` becomes the id `alice` and the display name `Alice`.

The user is asked to accept the proposal. Answering no lets them type both values by hand.

One name is reserved. A directory named `bountiful` would give the agent the id `bountiful`, which collides with the shared infrastructure directory at `~/.bountiful/`. When build.py sees that name, it asks for a different agent id before proposing anything, so a user who clones the repository without renaming it can still proceed.

Before writing anything, build.py checks whether `~/.{id}/` already exists. If it does, another agent on the machine already uses that name, and build.py stops with a suggested new directory name rather than letting two agents share one memory.

Once the name is settled, build.py writes the id and display name into `dashboard.json`, writes the id into `pyproject.toml` as the package name, and removes the `.github/` directory, which holds the template's funding metadata and has no purpose in a user's agent. The sentinel is gone, so the naming step never runs again.

## What the id controls

The id is the agent's single source of identity. Its memory database lives at `~/.{id}/{id}.db`. Its Anthropic API key, if one is added, is stored in the keyring under the id. Every log line begins with the id in brackets. The display name is what the agent is called in the interface and in its persona, where `{{ name }}` is replaced with it.


The id locates the database. Changing it later in `dashboard.json` does not move the agent's memory. At the next startup, the engine creates a new, empty database under the new id, while the old conversations remain untouched in the old directory. The Anthropic key is stored under the id as well, so it would need to be entered again. To change only what the agent is called, edit the display name and leave the id alone.


## Example

```
git clone https://github.com/CablepunkPress/bountiful.git alice
cd alice
python build.py
Naming this agent: Alice (id: alice)
Accept? [Y/n]
```

The repository directory is `alice/`, the agent's id is `alice`, its memory will live at `~/.alice/alice.db`, and its log lines will begin with `[alice]`.