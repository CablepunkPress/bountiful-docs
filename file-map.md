# Bountiful File Map

Every file across all four repos, annotated.
Last updated: September 2026


## bountiful

bountiful/
├── .github/
│   └── FUNDING.yml       # GitHub funding file; build.py removes for end user
├── tools/
│   └── TOOLS.md          # Explains box tool structure
├── .gitignore
├── add_secrets.py        # Shim → basic_bot.setup.secrets.run()
├── add_tools.py          # Shim → basic_bot.setup.tools.run()
├── build.py              # First-run setup: name, venv, pip, infrastructure
├── config.toml           # Agent overrides: provider, port, model
├── dashboard.json        # Agent identity: id, name
├── LICENSE
├── persona.md            # Agent personality, user-authored
├── pyproject.toml        # Pins basic-bot and basic-ui versions
├── README.md             # End-user quickstart
├── run.py                # Shim → basic_ui.launch.launch()


## basic-bot

basic-bot/
├── .github/
│   └── FUNDING.yml
├── basic_bot/
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── llamacpp.py       # Clone and compile llama.cpp from source
│   │   ├── orchestration.py  # Fold lifecycle — sequential server management
│   │   └── server.py         # llama-server start, stop, health check
│   ├── instructions/
│   │   └── capabilities.md   # Engine-owned system prompt section
│   ├── profiles/
│   │   └── nvidia_12gb.toml  # Hardware profile: models, launch args, sampling
│   ├── providers/
│   │   ├── __init__.py
│   │   ├── claude.py         # ClaudeProvider — Anthropic API
│   │   ├── local.py          # LocalProvider — llama-server HTTP client
│   │   ├── protocol.py       # InferenceProvider protocol, ChatResponse, ModelInfo
│   │   └── registry.py       # ChatProviderRegistry — composite provider with lifecycle
│   ├── setup/
│   │   ├── __init__.py
│   │   ├── secrets.py        # API key storage via keyring
│   │   └── tools.py          # Tool group installation from extend-a-bot
│   ├── tool_belt/
│   │   ├── __init__.py
│   │   ├── recall_message.py # Deterministic lookup by seq, range, or date
│   │   └── search_archive.py # Semantic vector search over RAG archive
│   ├── __init__.py
│   ├── __main__.py           # Build orchestrator: hardware, llama.cpp, models
│   ├── chat.py               # Chat loop, system prompt, tool execution
│   ├── config.py             # Engine defaults, overridable via config.toml
│   ├── diagnostics.py        # Memory snapshots for fold debugging
│   ├── embeddings.py         # Embedder protocol, LocalEmbedder, ManagedEmbedder
│   ├── factory.py            # create_runtime() — builds BotRuntime from agent dir
│   ├── fold.py               # Fold trigger logic, RAG + summary coordination
│   ├── memory.py             # Context builder — window, summary, system prompt
│   ├── profile.py            # Hardware detection, profile loading, model catalog
│   ├── rag.py                # Turn pairing, embedding, vector search
│   ├── runtime.py            # BotRuntime dataclass
│   ├── secrets_env.py        # Load API keys from keyring into environment
│   ├── store.py              # MessageStore protocol
│   ├── store_sqlite.py       # SQLite implementation — messages, state, vectors
│   ├── summary.py            # Rolling summary prompt and generation
│   └── tools.py              # Tool registry — belt + box discovery
├── scripts/
│   ├── backfill_rag.py       # Legacy: backfill RAG vectors
│   ├── backfill_seq.py       # Legacy: backfill sequence numbers
│   ├── rebuild_summary.py    # Regenerate rolling summary from scratch
│   ├── reembed.py            # Re-embed all vectors after model change
│   ├── test_fold.py          # Manual fold verification
│   ├── test_fold_lifecycle.py # Manual server lifecycle verification
│   └── test_rag.py           # Manual RAG verification
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md


## basic-ui

basic-ui/
├── basic_ui/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css    # Dark-mode styles, responsive layout
│   │   └── js/
│   │       ├── chat.js       # Message handling, model selection, history
│   │       ├── globals.d.ts  # TypeScript declarations for Pyright
│   │       └── jsconfig.json # JS project config
│   ├── templates/
│   │   └── index.html        # Agent name injected via Jinja2
│   ├── __init__.py
│   ├── app.py                # Flask routes: /chat, /models, /history
│   ├── config.py             # UI defaults: port, debug, reloader
│   └── launch.py             # Local launch orchestrator: secrets, servers, Flask
├── .github/
│   └── FUNDING.yml
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md


## extend-a-bot

extend-a-bot/
├── .github/
│   └── FUNDING.yml
├── github/
│   ├── _auth.py              # GitHub App auth, token caching, normalize_repo()
│   ├── _config.py            # User-editable: org, committer identity, co-author
│   ├── create_branch.py
│   ├── create_or_update_file.py
│   ├── create_pull_request.py
│   ├── delete_branch.py
│   ├── delete_file.py
│   ├── get_commit_history.py
│   ├── get_repo_info.py
│   ├── list_branches.py
│   ├── list_repo_contents.py
│   ├── list_repos.py
│   ├── merge_pull_request.py
│   ├── read_file.py
│   └── tool.json             # Manifest: dependencies, secrets, config files
├── .gitignore
├── LICENSE
├── README.md
└── version.json
