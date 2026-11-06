# The setup

The setup is what `python3 build.py` does. It runs in two halves. `build.py`, in the bountiful repository, sets up Python and the `bountiful` command. In the middle, it hands over to basic-bot's build, which sets up llama.cpp, the profile, and the models.

The same setup runs to install Bountiful, to finish an install that stopped, and to rebuild after an update. Each step checks what's already done and skips it.

## The question

`build.py` first says what it will install, and asks one question: `Install Bountiful? [Y/n]`. The answer is recorded in `~/.bountiful/install.json`, so a later run doesn't ask again.

If no one is at the keyboard, such as when another program runs the setup, it installs without asking. In that case it leaves your shell's startup file alone and records nothing.

## 1. Python environment

`build.py` makes a virtual environment, the `.venv` folder in the clone. It must run with Python 3.14 or newer, and stops with a message if it isn't.

It installs the bountiful package into the venv with pip. pip reads bountiful's pins and installs basic-bot, basic-ui, and extend-a-bot from GitHub, along with what they need from the Python Package Index.

On every run, it installs Bountiful's own parts again from scratch. pip would otherwise skip a part whose version number hasn't changed, even when its pin now points to newer code.

If the system's Python has moved to a new version since the venv was made, the venv is thrown away and made again.

The first time, it also makes the clone pull-only, so nothing can be pushed from it to GitHub.

## 2. basic-bot's build

`build.py` now runs `python -m basic_bot`, which does the next four steps.

### Agents' tools

Custom tools can need Python packages of their own. Each tool group lists them in its `tool.json`. The build installs them for every registered agent. On a first install there are no agents, so this step prints nothing.

### llama.cpp

The build checks that the tools for building llama.cpp are installed: Apple's Command Line Tools and cmake on a Mac, or cmake, a compiler, and Vulkan's files on GNU/Linux.

Then it downloads llama.cpp's source code into `~/.bountiful/llama.cpp`. The version is pinned twice: by its tag, such as `v0.7.0`, and by the exact commit that tag must point to. A tag is only a label and can be moved, so the build checks the commit before it compiles anything.

It compiles only `llama-server`, with Metal on a Mac or Vulkan on GNU/Linux.

When it's done, it writes the version and the build settings to `~/.bountiful/llama.cpp/.bountiful-version`. A later run rebuilds llama.cpp only if the pin or the settings have changed.

### Hardware profile

The build works out what kind of computer this is:

- **The backend** comes from the operating system: Metal on a Mac, Vulkan on GNU/Linux.
- **The memory for models** is a Mac's memory, or on GNU/Linux the memory of the largest graphics card. On GNU/Linux the build asks the `llama-server` it just compiled, which is why llama.cpp is built first.

Profiles come with basic-bot, as files in `basic_bot/profiles/`. Each one says what kind of computer it needs. The build picks the largest profile for this backend that fits the memory, and writes its choice to `~/.bountiful/machine.toml`. Every agent on the computer uses that profile.

### AI models

The build downloads the models the profile names into `~/.bountiful/models`: the embedding model, the summary model, and the chat model.

Each model file is pinned in the profile by its exact version on Hugging Face, its size, and its checksum. A checksum is a long number worked out from a file's contents, so a file that's been damaged or changed gives a different one. After a download, the build checks the file's checksum, and records the files that passed in `~/.bountiful/models/.verified.json`, so later runs don't need to check 30 GB of files again.

A download that stops is kept as a `.partial` file and carries on from where it was on the next run. A dropped connection is retried on its own.

On a computer that's already set up, a download of more than 5 GB asks first. This happens when an update brings a new chat model.

## 3. The bountiful command

Back in `build.py`, the last step links `~/.local/bin/bountiful` to the `bountiful` command inside the venv. If a different file is already there, it's left alone.

If `~/.local/bin` isn't on your PATH, the build adds one line to the end of your shell's startup file, such as `~/.zshrc`, and records that it did so in `install.json`. If you remove the line later, the build doesn't add it again. For a shell it doesn't know, it prints the line for you to add.

The command comes last, so the setup never leaves a `bountiful` command behind without the parts it needs.

## The records it leaves

| File | What it holds |
| --- | --- |
| `~/.bountiful/install.json` | Your answer to the question, and whether the setup added the PATH line. |
| `~/.bountiful/llama.cpp/.bountiful-version` | Which llama.cpp was built, and how. |
| `~/.bountiful/machine.toml` | The profile this computer uses. |
| `~/.bountiful/models/.verified.json` | Which model files have passed their checksum. |
