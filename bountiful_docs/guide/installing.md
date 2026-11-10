# Installing Bountiful

Installing Bountiful takes three steps. First you get your computer ready. Then you download Bountiful. Then you run its setup, which does the rest.

## What you need

Bountiful runs AI models on your own computer, so it needs a strong one. It is tested on two kinds of machine:

- An Apple Mac Mini with an M6 chip and 32 GB of memory.
- A GNU/Linux computer with an Nvidia GeForce RTX 3060 graphics card (12 GB) and 32 GB of system memory.

You also need about 35 GB of free disk space for the AI models, and an internet connection to download them.

## Get your Mac ready

Bountiful needs three programs that a Mac doesn't come with:

- **Homebrew**, which installs other programs for you.
- **Python**, the language Bountiful is written in. It must be version 3.14 or newer.
- **cmake**, which Bountiful uses to build llama.cpp, the program that runs the AI models.

Open the Terminal app. Paste this command from [Homebrew's website](https://brew.sh/) and press Return:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Homebrew's installer also installs Apple's Command Line Tools. These give you git, which downloads Bountiful, and a compiler, which builds llama.cpp.

When the installer finishes, it shows a few commands under "Next steps". Run them. Without them, your terminal can't find the `brew` command.

Now install Python and cmake, and check which Python you have:

```bash
brew install python cmake
python3 --version
```

It should say Python 3.14 or newer. If it shows an older version, run Homebrew's "Next steps" commands again and open a new terminal window. Your Mac comes with an older Python of its own, and the terminal finds that one until Homebrew's is set up.

## Get your GNU/Linux computer ready

On GNU/Linux, Bountiful builds llama.cpp to use your graphics card through Vulkan. Vulkan is a standard way for programs to talk to graphics cards. You need Python, git, cmake, a C++ compiler, and Vulkan's development files.

On Arch and CachyOS:

```bash
sudo pacman -S python git cmake gcc vulkan-headers shaderc spirv-headers
```

On Debian and Ubuntu:

```bash
sudo apt install python3 python3-venv git cmake g++ libvulkan-dev glslc spirv-headers
```

To check that Vulkan can see your graphics card, run `vulkaninfo --summary`. It comes in the `vulkan-tools` package. Your card should be in the list.

Then check which Python you have:

```bash
python3 --version
```

It should say Python 3.14 or newer.

## Download Bountiful

Bountiful is downloaded with git. This makes a copy of it called a clone. Put it in your home folder:

```bash
cd ~
git clone https://github.com/CablepunkPress/bountiful.git
cd bountiful
```

You don't need a GitHub account. Use `git clone` rather than downloading a zip file, because Bountiful updates itself through git.

## Run the setup

Start the setup:

```bash
python3 build.py
```

The setup first tells you what it will do, and asks one question:

```
Install Bountiful? [Y/n]
```

Press Return to say yes. After that it doesn't ask anything else. It works through these steps, and prints a heading for each one:

1. **Python environment.** It makes a private space for Bountiful's Python code, in the `.venv` folder inside the clone. It installs Bountiful's parts from GitHub into it.
2. **llama.cpp, the inference server.** It downloads llama.cpp and builds it for your computer. Inference means running an AI model to get an answer. This step takes several minutes and prints many lines.
3. **Hardware profile.** It looks at your computer and picks the settings that suit it. These settings are called a profile.
4. **AI models.** It downloads the three AI models every agent needs. One is for chatting. One summarizes older parts of a conversation. One helps an agent search its memory. Their sizes are shown before the download starts.
5. **The bountiful command.** It installs the `bountiful` command, so you can type `bountiful` in any terminal.

On a slow connection, the downloads can take hours. You can leave the setup running on its own.

If the setup stops partway, for example because the connection dropped or you pressed Control-C, run `python3 build.py` again. It picks up where it stopped, and partly downloaded models carry on from where they were.

## When the setup is done

The setup ends with:

```
Setup complete. Open a new terminal window, then type 'bountiful' to begin.
```

Open a new terminal window. The old one doesn't know about the `bountiful` command yet. In the new one, type:

```bash
bountiful
```

It shows the list of commands. Bountiful is installed, and you're ready to create your first agent.

## Where everything went

- **The clone**, `~/bountiful`, holds Bountiful itself.
- **`~/.bountiful`** holds llama.cpp, the AI models, and Bountiful's records. The dot at the start of its name hides it in most file browsers.
- **The `bountiful` command** is in `~/.local/bin`. The setup adds that folder to your PATH, the list of folders your terminal searches for commands. It does this with one line at the end of your shell's startup file, such as `~/.zshrc` on a Mac.
