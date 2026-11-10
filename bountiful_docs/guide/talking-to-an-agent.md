# Talking to an agent

You talk to an agent in your web browser. The terminal starts it and stops it.

## Start the agent

Type `bountiful`, followed by the agent's ID:

```bash
bountiful alice
```

The terminal shows what Bountiful is doing while it starts the agent. When it's ready, the last line says:

```
Starting the web page at http://localhost:11777
```

Open http://localhost:11777 in your web browser. The page comes from your own computer, not the internet, so only you can open it.

Only one agent can run at a time.

## Send a message

Type in the box at the bottom of the page and press Send.

## The agent's memory

The agent remembers your conversations, even after you stop it and start it again.

When a conversation gets long, the page sometimes says "Updating memory…" after a reply. The agent is writing a summary of the older part of the conversation. When the page says "Memory updated.", you can carry on.

## Stop the agent

Go back to the terminal and press Control-C.

Closing the browser tab doesn't stop the agent. It keeps running until you press Control-C or close the terminal window.
