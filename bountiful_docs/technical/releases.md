# Releases and versions

## Tags and pins

A tag is a label git puts on one exact version of a repository. Each Bountiful release is a tag on the bountiful repository, such as `v0.8.0`.

At that tag, bountiful's `pyproject.toml` pins a tag of each other part:

```toml
dependencies = [
    "basic-bot @ git+https://github.com/CablepunkPress/basic-bot.git@v0.11.0",
    "basic-ui @ git+https://github.com/CablepunkPress/basic-ui.git@v0.7.0",
    "extend-a-bot @ git+https://github.com/CablepunkPress/extend-a-bot.git@v0.3.0",
]
```

So one bountiful tag names the exact version of every part, and the setup installs exactly those. A release tag never moves, so it always means the same code.

## Two branches

bountiful has two branches:

- **`stable`** always points at the newest release. A new clone starts on it.
- **`main`** is where new work happens before it's released. Its pins are `@main` instead of tags, so a clone on `main` gets the newest code of every part.

The other parts, basic-bot, basic-ui, and extend-a-bot, have only `main`. Nobody clones them to use Bountiful. bountiful's pins reach them.

## Version numbers

Every part has its own version number, in its `__init__.py`. The numbers don't have to match: bountiful `v0.8.0` pins basic-bot `v0.11.0`. Between releases, the version on `main` ends in `.dev0`, such as `0.9.0.dev0`.

`bountiful version` prints the version of bountiful installed in the venv.

`bountiful update` moves a clone on `stable` to the newest release, and runs the setup again to install it. [The bountiful command and the registry](command-and-registry.md) explains what it checks first.
