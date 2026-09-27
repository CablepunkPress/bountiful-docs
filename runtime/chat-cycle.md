# The Chat Cycle

The chat cycle is what happens between the moment a user sends a message and the moment the reply appears. It is the most frequent path through the engine, and every other runtime behavior, the fold and the search cycle, happens inside or right after it.

## From message to prompt

The interface sends the message to the `/chat` route along with the user's chosen model, effort level, and Deep Reasoning setting. The route hands everything to `chat_with_model` in chat.py. If the requested model isn't available, the engine quietly substitutes the default.

The engine then loads the sliding window: every stored message after the summary boundary, followed by the new message. Each message is prefixed with an HTML comment such as `<!-- seq:1542 -->` that records its permanent sequence number.

The prompt is assembled in order from the most stable material to the most volatile. The inference server can reuse its cached computation for everything up to the first part that changed since the previous request, so the parts that change every turn go last, where they cannot invalidate anything behind them.

```
system prompt (stable)
  # PERSONA        persona.md
  # CAPABILITIES   instructions/capabilities.md
  # OUTPUT         instructions/output.md
  # CONTEXT        context/*.md, only when files exist
  # TOOLS          tool count and names, fixed at startup
  # MEMORY         rolling summary; changes only at a fold
  [tool schemas]   placed by the chat template
messages (append-only)
  sliding window, oldest to newest
  newest user message
    + turn note    current model, effort, and Deep Reasoning
```

The turn note is an HTML comment the system appends to the newest message. It states which model the agent is running on and how it is configured, and it is the one place that information appears. It exists only in the prompt. The database stores exactly what the user typed.

## Inference and tools

The chat provider is a registry that holds every available model, local and API alike. When the requested model differs from what is currently loaded, the registry stops or starts the local chat server as needed before the call, so switching models in the interface costs nothing until a message is actually sent.

The model either replies or asks for tools. When it asks, the engine runs each tool, appends the results to the conversation, and calls the model again, repeating until the model answers without requesting any. A tool that fails returns its error to the model rather than crashing the turn. Most tools leave the chat server running, but search_archive needs the embedding server, so it stops chat, embeds the query, and starts chat again before the loop continues.

If the call fails outright, the engine retries once with the provider's fallback model, without effort or Deep Reasoning, using a fresh copy of the conversation so nothing from the failed attempt carries over.

## After the reply

The interface route saves the exchange: the user's original message and the reply, with metadata recording which model answered and whether it reasoned. It then checks whether the sliding window has reached its ceiling. If it has, the fold runs before the reply is returned, so the user waits through it. Otherwise the reply goes straight back to the interface.

Every inference call logs its token usage, and when `log_reasoning` is enabled in config.toml, the model's reasoning appears in the terminal as well.
