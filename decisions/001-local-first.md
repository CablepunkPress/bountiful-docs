# 001: Local First

Status: Accepted
Date: October 2026

## Context

Most AI assistants are cloud services where the model runs remotely in a data center, and conversations are stored within a corporation's systems. Users only rent access to an assistant whose memory they don't own, and which stops working or otherwise becomes inaccessible when the service's rules change, its price is raised, or it gets discontinued. The user doesn't own their data, the corporation does, and downloading a copy of what should belong to the user can range from easy enough to downright tedious.

Bountiful is meant to be the user's own agent: a digital entity that exists on their machine, remembers their conversations for years, and keeps working without any corporation's permission.

## Decision

Everything the agent needs to function runs on the user's machine. Inference runs through llama.cpp on local hardware. Embeddings are computed locally. The agent's memory — every message, summary, and embedding — resides in a single SQLite database at `~/.{id}/{id}.db`. The core engine has no required dependencies on any cloud service.

Anything that reaches beyond the machine, such as an API model call or a search of the web, is an add-on the user installs deliberately and, where it needs one, supplies their own key for. None of the user's data leaves the machine unless the user chooses to add a feature that requires it.

## Consequences

The user owns their agent completely, and they are responsible for it. The agent's memory lives in one folder, `~/.{id}/`, which they should back up. Their agent works offline and can be moved from machine to machine. No corporation can read the stored conversations or take them away. However, if the user adds a connector to an outside model such as Claude, the messages sent through it do leave the machine by the user's choice.

The agent needs capable hardware, and that doesn't come cheap. Bountiful was prototyped on an Nvidia GeForce RTX 3060 12GB — hardware that was on hand. A machine with 32GB of memory is the current intended target. On constrained equipment, only one model fits in memory at a time, so the engine starts and stops model servers in sequence, which costs seconds at every fold and memory search. Speed has been traded for larger models at higher precision.

Local models are smaller than frontier cloud models, and they have quirks of their own. Where a larger model can power through a vague prompt or an oversized document, a local model needs clearer instructions and smaller pieces. Bountiful's design has been shaped around getting the most out of limited consumer hardware.

The engine must stay free of cloud dependencies. Its core runs on Python's standard library alone, so its dependency list is empty, and anything that reaches beyond the machine declares its own dependencies in the add-on that needs it. The engine is local-first: its local implementations ship with it and are used by default, while its provider and store abstractions keep other deployments possible later without changing the core.
