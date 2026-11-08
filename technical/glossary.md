# Glossary

What the words in these docs mean. These are also the names we've agreed on, for the docs, the docstrings, and the READMEs.

**Agent.** An AI model plus a harness. The harness gives the model a name, a persona, memory, and tools, so it becomes something you can talk to over time. We say agent, not assistant.

**Agent folder.** The folder that holds one agent, such as `~/alice`. Everything that belongs to that agent is in it.

**Annotation.** A hidden note at the start of each message in the prompt, giving its number, when it was written, and, for a reply, which tools it used.

**API key.** A secret code, like a password, that lets a program use an online service on your account.

**Archive.** Every message an agent and its user have exchanged, kept word for word in its database, which the agent searches with its memory tools.

**Backend.** How llama.cpp uses a computer's graphics chip: Metal on a Mac, Vulkan on GNU/Linux.

**Branch.** A line of work in a git repository. Bountiful's releases go to `stable`. New work goes to `main` first.

**Chat model.** The AI model the agent talks with.

**Chat template.** The part of a model that lays out its prompt in the form the model was trained on, including where the tools go.

**Clone.** A copy of a git repository on your computer, made with `git clone`.

**Context.** The notes in an agent's `context/` folder, which the agent is given every turn.

**Context window.** How much text a model can hold in mind at once, measured in tokens.

**Custom tools.** Tool groups the user writes, kept in `~/bountiful/custom/tools/`. Also called the tool shed.

**Default tools.** The tools every agent has, such as searching its past conversations. They come with basic-bot. Also called the tool belt.

**Drafter.** A small, fast helper that guesses the chat model's next few tokens, so the chat model can check several at once and answer faster.

**Embedding.** A long list of numbers that stands for what a piece of text means. Texts with similar meanings get similar embeddings.

**Embedding model.** An AI model that turns text into a list of numbers, so texts with similar meanings get similar numbers. It lets an agent search by meaning.

**Fold.** Moving the older part of a conversation into the summary, so the conversation fits in the chat model's context window. The web page shows a fold as "Updating memory…".

**Front end.** What you use to talk to an agent, such as the web page or the terminal. Every front end goes through the session.

**Harness.** The software that turns an AI model into an agent. In Bountiful, the harness is basic-bot. We say harness, not engine.

**Hub.** The bountiful repository, which holds the setup and the `bountiful` command, and pins every other part.

**ID.** The short name of an agent for typing, such as `alice`. It names the agent's folder.

**Inference.** Running an AI model to get an answer.

**Jack.** A fixed place in basic-bot where another part plugs in. The tools jack takes tools; the model jack takes providers.

**Keyring.** The safe place your computer keeps passwords and keys, such as the Keychain on a Mac.

**KV cache.** A model's working memory of the prompt it has read, kept by its server so it doesn't have to read the same text again.

**llama.cpp.** The open-source program that runs the AI models. Bountiful builds it for your computer.

**llama-server.** llama.cpp's server. Bountiful runs one for each of the three models.

**Metal.** Apple's way for programs to use a Mac's graphics chip. llama.cpp uses it on a Mac.

**Name.** What an agent is called, such as `Alice`. It can have capitals and spaces.

**Persona.** The description of an agent's personality, in its `persona.md`.

**Pin.** Naming the exact version of a part that Bountiful uses.

**Plugin tools.** Tools that come in an installed package, such as extend-a-bot's Wikipedia and Brave Search. Also called the tool box.

**Port.** A numbered door on a computer that a program listens on.

**Prefill.** The opening words of a model's reasoning, given to it at the start of every turn.

**Profile.** The settings that suit a kind of computer: which models to use and how to run them. Setup picks one, such as `metal_32gb` or `vulkan_12gb`.

**Prompt.** Everything the model is given before it answers: the persona, the instructions, the context, the summary, the recent conversation, and your message.

**Provider.** What answers a model's requests. Today the only provider is llama-server on your computer.

**Registry.** Bountiful's list of the agents on your computer, kept in `~/.bountiful/agents.json`.

**Release.** A finished version of Bountiful, marked with a tag such as `v0.8.0`.

**Repository.** A project's files and their history, kept with git.

**Runtime.** Everything that makes an agent itself while it runs: its prompt, its tools, its database, and its models. The session is built on it.

**Session.** A running agent, from the moment you start it to the moment you stop it. The web page, and any other front end, talks to the agent through its session.

**Slot.** The chat server's saved cache, kept in the agent's `data/slots/` folder between restarts.

**Summary.** The agent's written account of the older parts of a conversation, kept up to date by folds.

**Summary model.** The AI model that writes the summary.

**Tag.** A label git puts on one exact version of a repository. Releases are tags.

**Token.** A piece of text, about three quarters of a word on average. Models read and write in tokens.

**Tool.** Something a model can use to do more than write text, such as searching Wikipedia.

**Tool group.** A set of tools that work together, added to an agent in one step, such as `wikipedia`.

**Turn.** One message from you and the agent's reply to it.

**Unified memory.** On a Mac, one pool of memory shared by the processor and the graphics chip.

**venv.** A virtual environment: a private copy of Python with its own installed packages. Bountiful's is the `.venv` folder in the clone.

**Warming.** Sending the conversation to the chat server ahead of time, so the next message is answered sooner.

**Vulkan.** A standard way for programs to use a graphics card. llama.cpp uses it on GNU/Linux.
