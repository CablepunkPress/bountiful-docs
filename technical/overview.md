# Overview

## Built on llama.cpp

Bountiful is built on llama.cpp, an open-source program that runs AI models on your own computer. Bountiful downloads llama.cpp and builds it for your computer during setup. It uses llama.cpp's server, `llama-server`, to run each model.

## The parts

Bountiful is made of several parts. Each part is its own repository on GitHub, and each one does one job.

**basic-bot** is the harness. A harness is the software that turns an AI model into an agent. It builds the prompt, runs the model, lets the model call tools, keeps the agent's memory, and stops anything from running too long. It also builds llama.cpp during setup, and starts and stops its servers.

**basic-ui** is the web page you chat on. It is a small web server, made with Flask, that shows the conversation and sends your messages to basic-bot.

**extend-a-bot** holds the plugin tools, such as Wikipedia and Brave Search, and the code that adds them to an agent and keeps their keys.

**bountiful** is the hub. It holds the setup, `build.py`, and the `bountiful` command. It also pins the other parts: it names exactly which version of each one Bountiful uses. A Bountiful release is one set of versions that work together.

**bountiful-docs** is this documentation. It will join the pinned parts, so every agent can read the docs for the version it runs.

## Who knows about whom

The parts depend on each other in one direction only:

- basic-bot knows about none of the others.
- basic-ui uses basic-bot.
- extend-a-bot uses basic-bot.
- bountiful uses all of them.

basic-bot never names extend-a-bot. Instead, it has jacks: fixed places where other parts plug in. extend-a-bot plugs its tools into basic-bot's tools jack.

## Where everything lives on your computer

- **`~/bountiful`** is the clone of the bountiful repository. Its `.venv` folder holds a private copy of Python with all the parts installed. Its `custom/` folder is for your own hardware profile and tool groups, and updates never change it.
- **`~/.bountiful`** holds llama.cpp, the AI models, and Bountiful's records, such as the list of agents.
- **`~/ID`** is each agent's folder, such as `~/alice`. It holds everything that belongs to that agent, including its memory.
- **`~/.local/bin/bountiful`** is the `bountiful` command, linked to the one inside `.venv`.

## The three models

Each agent uses three AI models, each one run by its own `llama-server`:

- **The chat model** talks with you and calls the tools. Its server listens on port 11555.
- **The summary model** writes the summaries that keep a long conversation within what the chat model can hold. Its server listens on port 11444.
- **The embedding model** turns messages into numbers, so the agent can search its past conversations by meaning. Its server listens on port 11333.

Only one of these servers runs at a time. The chat model's server runs while you talk, and stops whenever the agent needs one of the other two.

A port is a numbered door on your computer that a program listens on. These servers only accept connections from your own computer.
