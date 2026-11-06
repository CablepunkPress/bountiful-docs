# Creating an agent

An agent is an AI you talk to. Each agent has its own name, its own personality, and its own memory of your conversations. You can make as many agents as you like.

## Create one

Open a terminal and type `bountiful create`, followed by the agent's name:

```bash
bountiful create Alice
```

Bountiful asks before it makes anything:

```
Create Alice with ID=alice at ~/alice? [Y/n]
```

Press Return to say yes. Bountiful makes the agent and tells you how to start it:

```
Created Alice at ~/alice.
Start Alice with 'bountiful alice'.
```

## The name and the ID

Every agent has two names.

- **The name** is what the agent is called, such as `Alice` or `Leeroy Jones`. It can have capital letters and spaces.
- **The ID** is a short version of the name for typing in the terminal, such as `alice` or `leeroy-jones`. Bountiful makes it from the name for you.

To make the ID, Bountiful uses lowercase letters, drops accents (Zoë becomes `zoe`), and turns spaces and other marks into hyphens (O'Brien becomes `o-brien`). A name needs at least one plain letter or number to make an ID from.

Each ID can only belong to one agent. If `alice` is already taken, or something in your home folder is already called `alice`, the new agent gets `alice-1` instead, then `alice-2`, and so on.

A few words can't be IDs, because Bountiful's commands use them, such as `create`, `agents`, and `update`. The word `bountiful` can't be an ID either.

## The agent's folder

Each agent lives in its own folder in your home folder, named after its ID. Alice lives in `~/alice`. Everything that makes Alice who she is is in that folder:

- **`agent.json`** holds the agent's ID and name.
- **`persona.md`** describes the agent's personality, in plain words. You can edit it. Where it says `{{ name }}`, the agent's name goes in.
- **`context/`** is a folder for notes the agent should keep in mind, such as background on a project. Its `_README.md` explains how to use it.
- **`.gitignore`** matters only if you keep the folder in git. It keeps the agent's memory out of git.

When you first start the agent, Bountiful adds a **`data/`** folder. It holds the agent's memory: its conversations and its logs.

Because each agent is just a folder, you can look inside it, edit it, and back it up like any other folder.

## Bountiful's list of agents

Bountiful keeps a list of the agents on your computer. Creating an agent adds it to the list. To see the list, type:

```bash
bountiful agents
```

It shows each agent's ID, name, and folder.
