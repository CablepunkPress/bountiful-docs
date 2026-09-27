# Bountiful File Map

Every file across the four repos, annotated. Directories come first, then files, alphabetically within each level, following Codium's order: names beginning with a dot or underscore sort before letters.

Last updated: September 2026


## bountiful

The agent template. Users clone it under their agent's name.

```
bountiful/
├── .github/
│   └── FUNDING.yml         # Funding file; build.py removes it on first run
├── context/
│   └── _README.md          # How to use context/; never loaded
├── tools/
│   └── _README.md          # How plugin tool groups work; never loaded
├── .gitignore
├── add_secrets.py          # Shim: store API keys in the keyring
├── add_tools.py            # Shim: install tool groups from extend-a-bot
├── build.py                # Name agent, build venv, install deps, infrastructure
├── config.toml             # Agent overrides of engine and UI defaults
├── dashboard.json          # Agent identity: id and display name
├── LICENSE
├── persona.md              # Agent personality, user-authored
├── pyproject.toml          # Pins basic-bot and basic-ui versions
├── README.md               # End-user quickstart
└── run.py                  # Shim: launch the agent
```


## basic-bot

The engine: memory, providers, tools, prompt assembly, infrastructure.

```
basic-bot/
├── .github/
│   └── FUNDING.yml
├── basic_bot/
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── llamacpp.py         # Clone and compile llama.cpp
│   │   ├── orchestration.py    # Fold with sequential server lifecycle
│   │   └── server.py           # llama-server start, stop, health check
│   ├── instructions/
│   │   ├── capabilities.md     # System prompt: memory and retrieval
│   │   └── output.md           # System prompt: reply formatting
│   ├── profiles/
│   │   └── nvidia_12gb.toml    # Hardware profile: models, launch args, sampling
│   ├── providers/
│   │   ├── __init__.py
│   │   ├── claude.py           # ClaudeProvider: Anthropic API
│   │   ├── local.py            # LocalProvider: llama-server client
│   │   ├── protocol.py         # InferenceProvider protocol, ModelInfo, ChatResponse
│   │   └── registry.py         # Composite chat provider; switches models and servers
│   ├── setup/
│   │   ├── __init__.py
│   │   ├── secrets.py          # Key prompts behind add_secrets.py
│   │   └── tools.py            # Tool group install behind add_tools.py
│   ├── tool_belt/
│   │   ├── __init__.py
│   │   ├── recall_message.py   # Lookup by sequence number, range, or date
│   │   └── search_archive.py   # Semantic search over the archive
│   ├── __init__.py
│   ├── __main__.py             # Build entry: hardware, llama.cpp, models
│   ├── chat.py                 # Prompt assembly, turn note, tool loop
│   ├── config.py               # Engine defaults, overridable in config.toml
│   ├── diagnostics.py          # Memory snapshots during a fold
│   ├── embeddings.py           # Embedder protocol, LocalEmbedder, ManagedEmbedder
│   ├── factory.py              # create_runtime(): assembles the BotRuntime
│   ├── fold.py                 # Fold trigger; embeds, then summarizes
│   ├── memory.py               # Loads the sliding window with seq annotations
│   ├── profile.py              # Hardware detection and profile loading
│   ├── rag.py                  # Turn pairing, embedding, truncation, search
│   ├── runtime.py              # BotRuntime dataclass
│   ├── secrets_env.py          # Loads the Anthropic key into the environment
│   ├── store.py                # MessageStore protocol
│   ├── store_sqlite.py         # SQLite store: messages, state, summaries, vectors
│   ├── summary.py              # Rolling summary prompt and generation
│   └── tools.py                # Tool registry: belt plus box
├── scripts/                    # Stale; to be revised, moved, or removed
│   ├── backfill_rag.py
│   ├── backfill_seq.py
│   ├── rebuild_summary.py
│   ├── reembed.py
│   ├── test_fold.py
│   ├── test_fold_lifecycle.py
│   └── test_rag.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```


## basic-ui

The reference web interface and local launch.

```
basic-ui/
├── .github/
│   └── FUNDING.yml
├── basic_ui/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css      # Page styles
│   │   └── js/
│   │       ├── chat.js         # Chat interface logic
│   │       ├── globals.d.ts    # Type declarations for the JS checker
│   │       └── jsconfig.json   # JS project settings for Codium
│   ├── templates/
│   │   └── index.html          # Page shell; agent name via Jinja2
│   ├── __init__.py
│   ├── app.py                  # Flask routes: /chat, /models, /history
│   ├── config.py               # UI defaults: port, debug, reloader
│   └── launch.py               # Local launch: overrides, keys, chat server, Flask
├── LICENSE
├── pyproject.toml
└── README.md
```


## extend-a-bot

Plugin tool groups, copied into an agent's tools/ directory.

```
extend-a-bot/
├── .github/
│   └── FUNDING.yml
├── github/
│   ├── _auth.py                  # GitHub App auth, token caching, normalize_repo()
│   ├── _config.py                # User-editable: org, committer, co-author
│   ├── create_branch.py
│   ├── create_or_update_file.py  # Commits only to a non-default branch
│   ├── create_pull_request.py
│   ├── get_commit_history.py
│   ├── get_repo_info.py
│   ├── list_branches.py
│   ├── list_repo_contents.py
│   ├── list_repos.py
│   ├── merge_pull_request.py     # Refuses; directs the user to review on GitHub
│   ├── read_file.py
│   └── tool.json                 # Manifest: dependencies, keys, config
├── .gitignore
├── LICENSE
├── README.md
└── version.json                  # Repo-wide version
```
