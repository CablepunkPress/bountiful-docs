# What leaves your computer

Bountiful runs its AI models on your own computer. Your conversations with your agents stay there.

## Your conversations

Everything you and your agents say is kept in each agent's folder, on your computer. The AI models that read and write it run on your computer too. No conversation is ever sent anywhere.

The web page you chat on is served by your own computer, and only your computer can open it. It loads nothing from the internet.

## Tools

What a tool sends depends on the tool:

- **The memory tools**, which search an agent's past conversations, send nothing anywhere.
- **wikipedia** sends what the agent searches for, and the titles of the articles it reads, to Wikipedia. Its requests name Bountiful as the program making them, not you. No account is needed.
- **brave** sends what the agent searches for to Brave Search, under your Brave Search API key. Brave charges for searches beyond its monthly free credit.

Only what the agent puts in a search is sent, not the conversation itself.

A custom tool, one you write or add yourself, sends whatever it was written to send.

`bountiful add` tells you what a tool group sends before it adds it.

## Keys

API keys, such as your Brave Search key, are kept in your computer's keyring, such as the Keychain on a Mac. They're never kept in the agent's folder.

## Installing and updating

The setup and `bountiful update` download Bountiful's parts and llama.cpp from GitHub, the Python packages they need from the Python Package Index, and the AI models from Hugging Face. They download only. Nothing about you or your agents is sent.
