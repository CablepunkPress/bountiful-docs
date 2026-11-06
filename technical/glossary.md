# Glossary

What the words in these docs mean. These are also the names we've agreed on, for the docs, the docstrings, and the READMEs.

**Agent.** An AI model plus a harness. The harness gives the model a name, a persona, memory, and tools, so it becomes something you can talk to over time. We say agent, not assistant.

**Agent folder.** The folder that holds one agent, such as `~/alice`. Everything that belongs to that agent is in it.

**API key.** A secret code, like a password, that lets a program use an online service on your account.

**Branch.** A line of work in a git repository. Bountiful's releases go to `stable`. New work goes to `main` first.

**Chat model.** The AI model the agent talks with.

**Clone.** A copy of a git repository on your computer, made with `git clone`.

**Context.** The notes in an agent's `context/` folder, which the agent is given every turn.

**Context window.** How much text a model can hold in mind at once, measured in tokens.

**Custom tools.** Tools the user writes, kept in the agent's `tools/` folder. Also called the tool shed.

**Default tools.** The tools every agent has, such as searching its past conversations. They come with basic-bot. Also called the tool belt.

**Embedding model.** An AI model that turns text into a list of numbers, so texts with similar meanings get similar numbers. It lets an agent search by meaning.

**Fold.** Moving the older part of a conversation into the summary, so the conversation fits in the chat model's context window. The web page shows a fold as "Updating memory…".

**Harness.** The software that turns an AI model into an agent. In Bountiful, the harness is basic-bot. We say harness, not engine.

**Hub.** The bountiful repository, which holds the setup and the `bountiful` command, and pins every other part.

**ID.** The short name of an agent for typing, such as `alice`. It names the agent's folder.

**Inference.** Running an AI model to get an answer.

**Jack.** A fixed place in basic-bot where another part plugs in. The tools jack takes tools; the model jack takes providers.

**Keyring.** The safe place your computer keeps passwords and keys, such as the Keychain on a Mac.

**llama.cpp.** The open-source program that runs the AI models. Bountiful builds it for your computer.

**llama-server.** llama.cpp's server. Bountiful runs one for each of the three models.

**Metal.** Apple's way for programs to use a Mac's graphics chip. llama.cpp uses it on a Mac.

**Name.** What an agent is called, such as `Alice`. It can have capitals and spaces.

**Persona.** The description of an agent's personality, in its `persona.md`.

**Pin.** Naming the exact version of a part that Bountiful uses.

**Plugin tools.** Tools that come in an installed package, such as extend-a-bot's Wikipedia and Brave Search. Also called the tool box.

**Port.** A numbered door on a computer that a program listens on.

**Profile.** The settings that suit a kind of computer: which models to use and how to run them. Setup picks one, such as `metal_32gb` or `vulkan_12gb`.

**Prompt.** Everything the model is given before it answers: the persona, the context, the summary, the recent conversation, and your message.

**Provider.** What answers a model's requests. Today the only provider is llama-server on your computer.

**Registry.** Bountiful's list of the agents on your computer, kept in `~/.bountiful/agents.json`.

**Release.** A finished version of Bountiful, marked with a tag such as `v0.8.0`.

**Repository.** A project's files and their history, kept with git.

**Session.** One run of an agent, from starting it to stopping it. In basic-bot, the session is also the one way every front end, such as the web page, talks to the agent.

**Summary.** The agent's written account of the older parts of a conversation, kept up to date by folds.

**Summary model.** The AI model that writes the summary.

**Tag.** A label git puts on one exact version of a repository. Releases are tags.

**Token.** A piece of text, about three quarters of a word on average. Models read and write in tokens.

**Tool.** Something a model can use to do more than write text, such as searching Wikipedia.

**Tool group.** A set of tools that work together, added to an agent in one step, such as `wikipedia`.

**Turn.** One message from you and the agent's reply to it.

**venv.** A virtual environment: a private copy of Python with its own installed packages. Bountiful's is the `.venv` folder in the clone.

**Vulkan.** A standard way for programs to use a graphics card. llama.cpp uses it on GNU/Linux.
