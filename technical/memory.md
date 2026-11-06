# Memory

An agent's memory works in three layers:

1. **The recent conversation**, word for word, in the prompt.
2. **The summary** of everything older, in the prompt's memory section.
3. **The archive** of every message ever exchanged, word for word, which the agent reaches with its memory tools.

All three are in the agent's database, `data/ID.db`.

Only one model server runs at a time. The summary model only runs in a fold, right after the embedding model. The embedding model is used in two places, a fold and `search_archive`. So there are only two patterns:

- **A fold:** chat stops → embedding runs, then stops → summary runs, then stops → chat starts again.
- **An archive search:** chat stops → embedding runs, then stops → chat starts again.

## The database

The database is one SQLite file. It has four tables:

| Table | What it holds |
| --- | --- |
| `messages` | Every message, yours and the agent's, with its number (`seq`), when it was written, and for a reply, the model that wrote it and the tools it used. |
| `state` | The current summary, the number of the last message it covers, and the number the next message will get. |
| `summaries` | Every summary the agent has written, oldest first. |
| `vectors` | The archive's search index: each pair of messages, a question and its reply, with its embedding. |

Nothing is ever deleted from `messages`. A fold adds to the summary and the archive, but every message stays in the database as it was written.

## The recent conversation

The prompt holds every message since the summary ends. That's never more than 40 messages, and after a fold it's 20. Both numbers are settings, `window_ceiling` and `window_floor`.

## Folds

When 40 messages have built up since the summary ends, a fold is due. The session tells the front end, and the web page shows "Updating memory…". A fold takes the oldest 20 of those messages and does two things with them:

1. **It adds them to the archive.** The chat model's server stops, and the embedding model's server starts. The embedding model turns each pair of messages into an embedding: a long list of numbers that stands for what the messages mean. The embeddings go in the `vectors` table. Then the embedding server stops.
2. **It rewrites the summary.** The summary model's server starts. The summary model is given the current summary and the 20 messages, and writes a new summary that takes them in. It's saved in `state` and added to `summaries`. Then the summary server stops, and the chat server starts again.

Once the new summary is saved, the summary ends 20 messages later than it did, and those 20 leave the recent conversation. The prompt goes back to 20 messages, and builds up to 40 again.

If either step fails, the summary doesn't move. The same 20 messages are folded again before the next message is answered.

## The summary

The summary keeps the gist: the important facts, preferences, and decisions. It's written to a fixed shape, a set number of paragraphs, so it doesn't grow longer with every fold. The archive keeps the exact words.

The summary model is shown which tools each reply used, the same way the chat model sees them in the annotations. This lets the summary tell what the agent looked up from what it said on its own.

A message far longer than usual is cut for the summary model, with a note saying how long it was. The message itself stays whole in the database.

## The archive and the memory tools

Every agent has two tools for reaching its archive.

**`search_archive`** searches by meaning. The agent gives it a few words, such as "the trip to Lisbon". The embedding model turns them into an embedding, and the archive finds the five pairs of messages whose embeddings are closest. Then it shows those messages, read from the `messages` table, best match first, each with its number. The chat server stops while the embedding server runs.

**`recall_message`** looks messages up exactly: by number, by a range of numbers, or by dates. Unlike `search_archive`, it reads the database directly and needs no model.

A message that's far longer than usual is shown cut, with a note saying how long it is. A result that would be too long shows as many messages as fit, and says how to ask for the rest.

The archive holds only the agent's conversations. It isn't a source of facts about the world, and the tools' descriptions tell the model so.
