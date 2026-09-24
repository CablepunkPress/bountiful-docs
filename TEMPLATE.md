# File-Tree Style Guide Template

Follow these rules when documenting repository structures:

1. **Directories at the top** - List all directories before any files
2. **Include dot files** - Show hidden files like `.gitignore`, `.env`, etc.
3. **Alphabetical order** - Sort everything alphabetically within each directory level

## Example Output Format

```
repo-name/
├── .github/
│   └── FUNDING.yml
├── .gitignore
├── README.md
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
└── tests/
    └── test_main.py
```

---
**Note**: This template reflects the style we established when reviewing `bountiful-docs/file-map.md`. Use this structure for all future file-tree documentation.