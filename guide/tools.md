# Tools

Tools let an agent do more than talk. With a tool, an agent can look something up instead of answering from what it already knows.

Every agent has tools for searching its own past conversations. You can add more, in groups called plugins. A tool group is a set of tools that work together.

## The tool groups

Bountiful comes with two plugins:

- **wikipedia** lets the agent search Wikipedia and read its articles. It needs no account.
- **brave** lets the agent search the web with Brave Search, for news and things Wikipedia doesn't cover. It needs a Brave Search API key.

To see the plugins, and which agents use each one, type:

```bash
bountiful tools
```

## Add a tool group

Type `bountiful add`, then the group, then the agent's ID:

```bash
bountiful add wikipedia alice
```

Bountiful first tells you what the tools send over the internet. Then it adds the group:

```
Added wikipedia to alice. It takes effect the next time alice starts.
```

If the agent is running, stop it and start it again to use the new tools.

## Add Brave Search

The brave group needs an API key. An API key is like a password that lets Bountiful use Brave's search service on your account. You get one by signing up for the Brave Search API on Brave's website. Brave gives a monthly free credit and charges for searches beyond it.

When you add the group, Bountiful asks for the key:

```bash
bountiful add brave alice
```

```
Paste the Brave Search API key (hidden):
```

Paste the key and press Return. The key stays hidden while you paste it. Bountiful keeps it in your computer's keyring, the safe place your system keeps passwords, such as the Keychain on a Mac.

To replace the key later, run `bountiful add brave alice` again.

## See an agent's tools

```bash
bountiful tools alice
```

This lists every tool the agent has: its memory tools, the tools every agent has, and the plugins added to it.

## Remove a tool group

```bash
bountiful remove wikipedia alice
```

This removes the group and its settings. For brave, it also deletes the API key from the keyring. Like adding, it takes effect the next time the agent starts.
