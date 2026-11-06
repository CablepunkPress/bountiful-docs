# Profiles

A profile is a file of settings for one kind of computer. It says which models to use, where to download them, and how to run each one. Every agent on a computer uses the same profile.

## The two profiles

Bountiful has two profiles, one for each kind of computer it's tested on:

| Profile | Computer | Backend | Memory for models |
| --- | --- | --- | --- |
| `metal_32gb` | an Apple Mac Mini with an M6 chip | Metal | 32 GB of unified memory |
| `vulkan_12gb` | a GNU/Linux computer with an Nvidia GeForce RTX 3060 | Vulkan | 12 GB on the graphics card, with 32 GB of system memory |

The backend is how llama.cpp uses the computer's graphics chip:

- **Metal** is Apple's way for programs to use a Mac's graphics chip. On a Mac, the graphics chip and the processor share one pool of memory, called unified memory, so the models can use most of it.
- **Vulkan** is a standard way for programs to use a graphics card. It works with cards from Nvidia, AMD, and Intel. A graphics card has its own memory, separate from the computer's system memory.

There are only profiles for computers that can be tested on real hardware. Each profile is made for, and run on, the machine in its name.

## How a profile is chosen

The setup chooses the profile once, as explained in [The setup](setup.md):

1. The operating system decides the backend: Metal on a Mac, Vulkan on GNU/Linux.
2. The setup measures the memory for models: a Mac's memory, or the largest graphics card's memory.
3. It picks the largest profile for that backend that fits the memory.

A computer with more memory than a profile needs uses that profile, and the setup says the combination is untested. A computer with less memory than the smallest profile needs can't run Bountiful, and the setup says how much is needed.

The choice is written to `~/.bountiful/machine.toml`. Each time an agent starts, it reads the profile named there.

## Where the profiles live

The profiles come with basic-bot, in `basic_bot/profiles/`, as TOML files: `metal_32gb.toml` and `vulkan_12gb.toml`. Each starts with a `[needs]` table that says what the computer must have:

```toml
[needs]
backend = "metal"
memory_gb = 32
```

## What's in a profile

A profile has one entry for each model: `[embedding]`, `[summary]`, and `[chat."ID"]` for the chat model. Each entry gives:

- **The download**: the file's name, its address on Hugging Face at an exact version, its size, and its checksum.
- **How to start its server**: such as how much of the model goes on the graphics chip, the context size, and the KV cache.

The chat model's entry has tables of its own:

- **`reasoning`**: how its reasoning is switched on, its budget, and its prefill.
- **`draft`**: its drafter, if it has one.
- **`sampling`**: how it picks each next word.

[The model servers](model-servers.md) explains what these settings do.

## How the two differ

Both profiles use the same chat model and the same embedding model. They differ where the hardware does:

- **The summary model** is Gemma 4 12B in both, a little smaller on GNU/Linux (Q5_K_M against Q6_K_L) to fit the 12 GB card.
- **The drafter** is only on the Mac.
- **The chat model** fits wholly in a Mac's memory. On the 12 GB card, llama.cpp keeps part of it in system memory, where the processor runs it.

Every profile is checked when the setup chooses it, and again each time an agent starts. A mistake in a profile is reported with a message that says what's wrong, before the agent starts talking.
