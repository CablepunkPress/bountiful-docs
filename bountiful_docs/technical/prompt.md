# The prompt

The prompt is everything the chat model is given before it answers. It has three parts: the system prompt, which tells the model who it is and what it knows; the tool definitions, which tell it what tools it has and how to call them; and the transcript, which is the conversation so far. basic-bot builds the system prompt and the transcript fresh for every message. The model's chat template adds the tool definitions between them.

The whole prompt, in order:

```
The system prompt
    1. The persona
    2. The instructions
    3. The context
    4. The tools list
    5. The memory
The tool definitions, added by the chat template
The transcript
    The conversation since the summary
    Your new message
```

## The system prompt

The system prompt is made of these sections, in this order:

1. **The persona**, from the agent's `persona.md`, with `{{ name }}` replaced by the agent's name.
2. **The instructions**, from basic-bot's `basic_bot/instructions/`. `capabilities.md` explains the agent's memory and how to use its tools. `identity.md` says what the agent is. `output.md` explains how to write its replies.
3. **The context**, from the agent's `context/` folder, under a `# CONTEXT` heading. It's left out when the folder has no files.
4. **The tools**, under a `# TOOLS` heading: a line naming every tool the agent has.
5. **The memory**, under a `# MEMORY` heading: the summary of the older part of the conversation, and which messages it covers. Until the first fold, it says that nothing has been summarized yet.

The first three sections are put together once, when the session opens. The memory section changes only when there's a fold.

## The transcript

After the system prompt comes the transcript: every message since the summary ends, word for word, and then your new message.

The messages go in as they were written, with nothing added. A reply that used tools comes after the calls it made, each followed by a short note in place of the tool's result, such as "Result from an earlier turn, not kept. The reply after it was written from it. To see it again, call the tool again." The note says instead when a call found nothing, failed, or wasn't run, and names the sites a result came from. The calls and notes are shown the way the model's chat template shows tool calls during a turn, so the model can see which of its replies came from a lookup, and what a real call looks like.

Each message also has a number, its place in the whole conversation starting at 1, and a time. The model sees these only when it asks for them with its memory tools, as part of their results.

Any note the model writes in its reply in the form `<!-- … -->` is taken out before the reply is saved, except inside a block of code.

## The tools

Section 4 of the system prompt, `# TOOLS`, is only a quick list of the tools' names. The full definitions come another way.

basic-bot sends each tool's name, description, and inputs to the chat model's server, separately from the system prompt. The server writes them into the prompt, using the model's chat template. The chat template is a part of the model that decides how the prompt is laid out, in the form the model was trained on.

The Gemma 4 chat template puts them at the end of the system prompt, after the memory section, so they're the last thing the model reads before the conversation.

## During a turn

When the model calls a tool, its call and the tool's result are added to the end of the transcript, and the model is asked again. This repeats until the model answers without calling a tool. The model's reasoning before each call is kept too, so it can follow its own plan through the turn.

Only the final reply is saved, with a record of the calls the turn made. The results last only for that turn. On later turns, each call is shown before the reply with its note in place of the result.

After 8 rounds of tool calls, set by `max_tool_rounds`, further calls aren't run. The model is told to answer with what it has found.

Sometimes the model plans to call a tool, then answers without calling it, and makes up what the tool would have found. basic-bot watches for this at the start of a turn. When the reply makes no call but writes one of the agent's tools out as if calling it, such as `search_archive(query="Gretel")`, even inside a made-up note, or when the model's reasoning names one of its tools and the reply doesn't name it at all, basic-bot sets the reply aside and asks again. A tool named in the reply in passing, as when the agent lists its tools, doesn't count. It gives the model its own reasoning back, with one more line in its own voice: that it planned to call the tool and hasn't yet, so it will call it now. This happens at most once a turn. It costs a second or two, and only on the turns that need it.

A reply can also run past the longest a reply may be, set by `max_tokens`. That only happens when something has gone wrong, such as the model repeating itself. The reply is then saved cut short, at 4,000 characters, with a note saying so, so it doesn't fill the conversation the agent rereads every turn.

## The reasoning prefill

The chat model's profile gives a prefill: the opening words of its reasoning. basic-bot starts the model's reasoning with those words on every turn, so it begins by planning its steps, with any tool call first, and by asking itself whether anything in the message should be checked with a tool.

## Why the order

The prompt goes from what changes least to what changes most: the persona and instructions never change while the agent runs, the memory changes only at a fold, and the transcript only grows at the end. The chat server keeps what it has already read, so each new message only has to add the part that's new.

Nothing that changes from turn to turn is written into the prompt. The model asks for the current time with its `date_and_time` tool, and the model and its settings reach the model through its server.
