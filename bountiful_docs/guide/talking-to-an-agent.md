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

## Interrupt the agent

If the agent is taking too long over a reply, open the drawer with the menu button at the top right and press **Interrupt Agent**. The agent stops at once. Your message is marked "Not sent" and goes back in the message box, so you can change it or send it again. The agent doesn't remember the interrupted turn.

## Stop the agent

Open the drawer and press **End Session**, or go back to the terminal and press Control-C. Either one stops the agent the same way.

Closing the browser tab doesn't stop the agent. It keeps running until you end the session, press Control-C, or close the terminal window.
