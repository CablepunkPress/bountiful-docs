# The prompt

The prompt is everything the chat model is given before it answers. basic-bot builds it fresh for every message, in two parts: the system prompt, which tells the model who it is and what it knows, and the transcript, which is the conversation so far.

The whole prompt, in order:

```
The system prompt
    1. The persona
    2. The instructions
    3. The tool groups' instructions
    4. The context
    5. The tools list
    6. The memory
The tool definitions, added by the chat template
The transcript
    The conversation since the summary
    Your new message
```

## The system prompt

The system prompt is made of these sections, in this order:

1. **The persona**, from the agent's `persona.md`, with `{{ name }}` replaced by the agent's name.
2. **The instructions**, from basic-bot's `basic_bot/instructions/`. `capabilities.md` explains the agent's memory and how to use its tools. `output.md` explains how to write its replies.
3. **The tool groups' instructions**, from each added group that has an `instructions.md`, such as Wikipedia's.
4. **The context**, from the agent's `context/` folder, under a `# CONTEXT` heading. It's left out when the folder has no files.
5. **The tools**, under a `# TOOLS` heading: a line naming every tool the agent has.
6. **The memory**, under a `# MEMORY` heading: the summary of the older part of the conversation, and which messages it covers. Until the first fold, it says that nothing has been summarized yet.

The first four sections are put together once, when the session opens. The memory section changes only when there's a fold.

## The transcript

After the system prompt comes the transcript: every message since the summary ends, word for word, and then your new message.

Each message starts with an annotation, a hidden note that tells the model which message it is and when it was written:

```
<!-- seq:107 created_at:2026-10-11T21:50:13+00:00 -->
```

- **`seq`** is the message's number in the whole conversation, starting at 1.
- **`created_at`** is when the message was written, in UTC.

An agent's reply also says which tools it used to write it, and which sites their answers came from:

```
<!-- seq:108 created_at:… tools:read_wikipedia(title="Brazil (1985 film)") → en.wikipedia.org -->
<!-- seq:110 created_at:… tools:none -->
```

`tools:none` means the reply was written without a tool.

The annotation on your new message is how the model knows the current time.

Annotations are added each time the prompt is built. They're never stored in the database, and the agent's replies are cleaned of any that the model writes.

## The tools

Section 5 of the system prompt, `# TOOLS`, is only a quick list of the tools' names. The full definitions come another way.

basic-bot sends each tool's name, description, and inputs to the chat model's server, separately from the system prompt. The server writes them into the prompt, using the model's chat template. The chat template is a part of the model that decides how the prompt is laid out, in the form the model was trained on.

The Gemma 4 chat template puts them at the end of the system prompt, after the memory section, so they're the last thing the model reads before the conversation.

## During a turn

When the model calls a tool, its call and the tool's result are added to the end of the transcript, and the model is asked again. This repeats until the model answers without calling a tool. The model's reasoning before each call is kept too, so it can follow its own plan through the turn.

Only the final reply is saved. The tool calls and their results last only for that turn. What stays is the record of which tools were used, which shows in the reply's annotation.

After 8 rounds of tool calls, set by `max_tool_rounds`, further calls aren't run. The model is told to answer with what it has found.

## The reasoning prefill

The chat model's profile gives a prefill: the opening words of its reasoning. basic-bot starts the model's reasoning with those words on every turn, so it begins by asking itself whether anything in the message should be checked with a tool.

## Why the order

The prompt goes from what changes least to what changes most: the persona and instructions never change while the agent runs, the memory changes only at a fold, and the transcript only grows at the end. The chat server keeps what it has already read, so each new message only has to add the part that's new.

Nothing that changes from turn to turn is written into the system prompt. The current time comes from the newest message's annotation, and the model and its settings reach the model through its server.
