# The model servers

Every AI model an agent uses runs in its own `llama-server`, llama.cpp's server. basic-bot starts each server when it's needed, talks to it over a port on your own computer, and stops it when it's done.

## The three servers

| Server | Port | Model on a Mac | Model on GNU/Linux |
| --- | --- | --- | --- |
| Chat | 11555 | Gemma 4 26B A4B QAT UD-Q4_K_XL | Gemma 4 26B A4B QAT UD-Q4_K_XL |
| Summary | 11444 | Gemma 4 12B Q6_K_L | Gemma 4 12B Q5_K_M |
| Embedding | 11333 | Nemotron 3 Embed 8B Q8_0 | Nemotron 3 Embed 8B Q8_0 |

The servers only listen on `127.0.0.1`, the address that means "this computer", so nothing else on your network can reach them.

Each session also makes a new, random API key, and gives it to every server it starts. A server refuses any request without the key, so a web page open in your browser can't use the servers, even though it runs on the same computer. The key is passed to each server privately, so it never appears in the server's logs. Only `/health`, which says whether a server is ready, answers without it.

The servers also run with `--no-slots`. This turns off `GET /slots`, a report of what a server is working on, which can include the conversation. Saving and loading the cache, described under "Slots" below, use a different address and still work.

Only one server runs at a time, because the models don't fit in memory together. The chat server runs while you talk. [Memory](memory.md) explains when the other two run.

## What the profile sets

The profile, chosen by the setup, says how to start each server: which model file to load, and the settings to start it with. For the chat model, the main settings are:

- **Context size**, 65,536 tokens: the most the chat model can hold in mind at once, the whole prompt and the reply together.
- **Reply length**, at most 4,096 tokens.
- **The KV cache**, kept in 8 bits. The KV cache is the model's working memory of the prompt it has read. Keeping it in 8 bits instead of 16 halves the memory it takes.
- **Reasoning**, with a budget of 1,024 tokens. When the model has reasoned that long, the server tells it to answer.
- **The reasoning prefill**, the opening words of its reasoning on every turn.
- **Sampling**: temperature 1.0, top-p 0.95, top-k 64, as Google recommends for Gemma 4. These settings decide how the model picks each next word.

On a Mac, the chat model also has a drafter. A drafter is a small, fast helper that guesses the next few tokens. The chat model checks all the guesses in one step and keeps the ones it agrees with. The answer is exactly the model's own, but it comes faster.

On GNU/Linux, the chat model doesn't all fit on a 12 GB graphics card. llama.cpp works out how much fits, and keeps the rest in the computer's system memory, where the processor runs it.

## Starting and stopping

basic-bot starts each `llama-server` with the command the profile describes, then waits until the server says it's ready.

Each server runs under a watchdog, a small program that starts the server and watches the agent. If the agent stops in a way that skips its normal shutdown, such as a crash or a force quit, the watchdog stops the server. A server never keeps running after its agent is gone.

Control-C in the terminal reaches only the agent, not the servers. The agent then stops them itself.

## The chat server's cache

The chat server keeps what it has read of the prompt, so the next message only has to add what's new. basic-bot keeps that cache across restarts in two ways.

**Slots.** Before the chat server stops, for a fold, an archive search, or the end of a session, basic-bot saves its cache to the agent's `data/slots/` folder. When the chat server starts again with the same setup, the cache is loaded back. Each saved file is named for the model and the exact way the server was started, so a cache is only ever loaded into the same setup. If saving or loading fails, the server simply reads the conversation again from the start.

**Checkpoints.** The server also keeps up to 4 checkpoints of its cache at earlier points in the prompt. When the end of the prompt changes, such as after a turn that used tools, the server can go back to a checkpoint instead of reading everything again.

**Warming** then readies the cache between turns. [The session](session.md) explains when it happens.

## Logs

Each time a server starts, it writes a new log in the agent's `data/logs/server/` folder. The log's name gives the time the server started, in UTC, and which model it ran. Its first line is the exact command that started the server. The newest 20 logs of each kind are kept.
