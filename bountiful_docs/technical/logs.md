# Logs

When something goes wrong, or you want to know what an agent did, the logs are where to look. Each agent keeps two kinds, in its `data/logs/` folder.

## The agent log

The agent log, `data/logs/agent/ID.log`, is a complete account of what the agent did. It's the same text the terminal shows while the agent runs.

Each line starts with the time, the agent's ID, the part of basic-bot that wrote it, and how serious it is:

```
2026-11-06 14:45:12,301 - [alice] basic_bot.session - INFO - Session opened: basic-bot 0.12.0.dev0, llama.cpp v0.7.0 (620d222), profile metal_32gb
```

The times are your computer's local time.

The log records:

- **Each session's start and end**, with the versions of basic-bot and llama.cpp, and the profile.
- **Each tool call**, by name.
- **Each fold**, step by step.
- **Each request to a model**, with how long it took.
- **Problems**, marked `WARNING` or `ERROR`.

A request's line says how much of the prompt the server already had, how much it read and how fast, how much it wrote and how fast, and whether the model reasoned:

```
Timing (Gemma 4 26B A4B QAT UD-Q4_K_XL): 12,480 cached, 97 read in 0.2 s (485/s), 312 generated in 6.1 s (51/s), drafter 0.58, reasoning yes
```

A turn that calls tools has one of these lines for each step. Warming writes the same kind of line, starting `Warmed`, with nothing generated.

When the log reaches 5 MB, it's renamed `ID.log.1`, and a new one starts. The three newest old files are kept, so the log never takes more than about 20 MB.

### The model's reasoning

The agent log can also record the model's reasoning and its reply, word for word, with why each reply ended: `stop` when the model finished, `tool_calls` when it called a tool, and `length` when it ran past `max_tokens`. It's off by default. To turn it on, add this line to the agent's `config.toml`, and start the agent again:

```toml
log_reasoning = true
```

## The server logs

The server logs, in `data/logs/server/`, are what the model servers themselves wrote. Each time a server starts, it gets a new log, named for when it started, in UTC, and which server it is:

```
2026-11-06-144512Z-chat-gemma-4-26b-a4b-it-qat-ud-q4_k_xl.log
2026-11-06-150203Z-embedding.log
2026-11-06-150219Z-summary.log
```

The first line of each is the exact command that started the server. The rest is llama.cpp's own output: loading the model, and every request it answered.

The newest 20 logs of each kind are kept.

## The record of tool calls

Which tools each reply used is saved in the agent's database, in the `tools` column of the `messages` table. [Tools](tools.md) explains what it holds. To read it for one message, such as message 108 of the agent `alice`:

```bash
sqlite3 -list ~/alice/data/alice.db "SELECT tools FROM messages WHERE seq = 108;" | python3 -m json.tool
```
