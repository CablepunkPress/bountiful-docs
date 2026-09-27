# Tool System

Tools are how an agent acts beyond producing text. Bountiful divides them into two kinds by a single question: does the tool stay on the user's machine, or does it reach outside it?

## Belt tools

Belt tools ship with the engine and are always loaded. There are two, search_archive and recall_message, and both let the agent read its own memory. search_archive finds past exchanges by meaning, and recall_message retrieves them by sequence number or date. Neither sends anything anywhere. They live in `basic_bot/tool_belt/`.

## Box tools

Box tools are optional groups the user deliberately installs. Every one of them connects to something outside the machine: GitHub, Wikipedia, and the Wild Wild Web. Since even a read-only box tool sends the agent's queries to someone else's server, none of these tools are installed by default. Installing a group, configuring it, and entering its keys is the user's decision and the user's risk.

Groups come from the extend-a-bot repository and are copied into the agent's own `tools/` directory, where the user can read and edit them. `python add_tools.py --list` shows what's available, `python add_tools.py github` installs a group, and `--update` refreshes the code while preserving the files listed as user configuration. The whole box can be switched off without uninstalling anything by setting `tool_box_enabled = false` in config.toml.

## Anatomy of a group

A group is a directory inside `tools/`. Every Python file in it that defines a `TOOL` dictionary and a `handler` function becomes a tool. Python files whose names begin with an underscore are shared modules the tools import, such as `_auth.py` for authentication and `_config.py` for the user's settings, and are never registered as tools themselves.

While a group loads, its directory is briefly added to Python's import path, so its tools can import their shared modules with a plain `from _auth import auth_headers`. When the group finishes loading, those shared modules are removed from Python's module cache. That is what lets two groups each have their own `_config.py` without one overwriting the other. A tool file that fails to load is logged and skipped, and the rest of its group loads normally.

Each group carries a `tool.json` manifest. It declares the group's Python dependencies, the keys it needs, and which files hold user configuration. The manifest is what add_tools.py reads to install dependencies, what add_secrets.py reads to prompt for keys, and what `--update` reads to know which files to leave alone.

The group's keys are stored in the system keyring under the service name its manifest declares, and the group's own code reads them from there. The GitHub group stores its keys under `github-tools`, which is not tied to any agent, so every agent on the machine that installs the group shares them.

A group's dependencies are installed into the agent's virtual environment, the one part of a group that lives outside `tools/`. Because a rebuilt environment starts empty, build.py reads every installed manifest on each run and reinstalls what they declare.

## Loading order

Belt tools load first, then box tools. If a box tool has the same name as a belt tool, the box tool replaces it. This lets someone customize how their agent searches its memory, but it also means an installed group could replace a belt tool without announcing it, so any group that defines search_archive or recall_message deserves a close read before installing.

## The handler contract

The engine calls every handler the same way, `handler(context, **tool_input)`, where the context carries the user id, the message store, and the embedder. Belt tools use the context. Box tools usually ignore it. The parameter is still required, because the engine never inspects a tool to decide how to call it.

A handler returns a string, usually JSON. Anything it raises is caught by the engine and returned to the model as an error, so a broken tool degrades one answer rather than the whole conversation.

## Read and construct, never destroy

The GitHub group is deliberately limited to reading and constructing. The agent can list repositories, read files and history, create branches, commit files to a branch, and open pull requests. It cannot commit to a repository's default branch, and its merge tool always declines, returning a link so the user can review the pull request on GitHub and merge it there. There are no tools for deleting files or branches.

This is a design choice, not a guardrail. Nothing asks the user to approve each action. The agent simply has no way to do lasting harm, so its initiative, which small models have in abundance, can only produce a branch and a proposal. It also narrows what the model must reason about on every turn: an agent with no destructive tools never spends effort deciding whether to destroy something.
