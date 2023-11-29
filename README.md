# ELO ratings

This is a Python script that calculates ELO ratings for a table tennis league.

## Player ratings

1. Per: 1216
2. Jannis: 1184

## Usage

1. Add new games to the `games.json` file using the following format:

```
[
  {
    "date": "2023-11-28",
    "result": {
      "John": 1,
      "Jane": 2
    }
  },
  ...
]
```

2. Run `./update.sh`
3. The script will calculate the ratings for all players and update the README.md file.
4. Commit and push the changes to GitHub to update the list.
