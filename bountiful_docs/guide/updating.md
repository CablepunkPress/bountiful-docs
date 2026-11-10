# Updating Bountiful

To get the newest version of Bountiful, type:

```bash
bountiful update
```

If there's nothing new, it says so:

```
Already up to date (v0.8.0).
```

If there's a new version, it tells you which one, shows what's changed, and asks:

```
Update? [Y/n]
```

Press Return to say yes. Bountiful downloads the new version and runs its setup again, the same setup you ran when you installed it. Your agents and their memories aren't touched.

To see which version you have, type:

```bash
bountiful version
```

## When it won't update

`bountiful update` only works on a clone made the way [Installing Bountiful](installing.md) describes. It stops if:

- **You've changed files in the clone.** It asks you to undo the changes first.
- **It can't reach GitHub.** Check your internet connection and try again.
- **The clone is on a different branch.** A branch is a version of the code that git keeps track of. New releases go to the `stable` branch, which is where a new clone starts. If you've switched to another branch, such as `main`, where new work happens before it's released, `bountiful update` leaves it alone.
