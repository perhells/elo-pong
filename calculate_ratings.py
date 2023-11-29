import json

input_file_path = "games.json"  # Change this to the path of your JSON input file

# JSON input file format:
# [
#   {
#     "date": "2023-11-28",
#     "result": {
#       "Jannis": 0,
#       "Per": 3
#     }
#   }
# ]

def print_readme():
    print("\n## Usage\n")
    print("1. Add new games to the `games.json` file using the following format:\n")
    print("```")
    print("[")
    print("  {")
    print("    \"date\": \"2023-11-28\",")
    print("    \"result\": {")
    print("      \"John\": 1,")
    print("      \"Jane\": 2")
    print("    }")
    print("  },")
    print("  ...")
    print("]")
    print("```\n")
    print("2. Run `./update.sh`")
    print("3. The script will calculate the ratings for all players and update the README.md file.")
    print("4. Commit and push the changes to GitHub to update the list.")


def calculate_elo_rating(player1_rating, player2_rating, sa):
    K = 32  # K-factor, a constant that determines the sensitivity of the rating change
    E_w = 1 / (1 + 10**((player2_rating - player1_rating) / 400))  # Expected probability of the player1 winning
    E_l = 1 / (1 + 10**((player1_rating - player2_rating) / 400))  # Expected probability of the player2 winning

    player1_new_rating = player1_rating + K * (sa - E_w)
    player2_new_rating = player2_rating + K * (1 - sa - E_l)

    return player1_new_rating, player2_new_rating

def update_ratings(player_ratings, game):
    players = list(game["result"].keys())

    if len(players) == 2:
        player1, player2 = players
        score1 = game["result"][player1]
        score2 = game["result"][player2]

        player1_rating = player_ratings.get(player1, 1200)  # Default rating is 1200
        player2_rating = player_ratings.get(player2, 1200)

        if score1 > score2:
            player1_new_rating, player2_new_rating = calculate_elo_rating(player1_rating, player2_rating, 1)
        elif score1 < score2:
            player1_new_rating, player2_new_rating = calculate_elo_rating(player1_rating, player2_rating, 0)
        else:
            player1_new_rating, player2_new_rating = calculate_elo_rating(player1_rating, player2_rating, 0.5)

        player_ratings[player1] = player1_new_rating
        player_ratings[player2] = player2_new_rating

    return player_ratings

def main():
    with open(input_file_path, "r") as file:
        games = json.load(file)

    player_ratings = {}  # Dictionary to store player ratings

    for game in games:
        player_ratings = update_ratings(player_ratings, game)

    print("# ELO ratings\n")
    print("This is a Python script that calculates ELO ratings for a table tennis league.\n")
    print("## Player ratings\n")

    i = 1
    for player, rating in sorted(player_ratings.items(), key=lambda item: item[1], reverse=True):
        print(f"{i}. {player}: {round(rating)}")
        i += 1

if __name__ == "__main__":
    main()
    print_readme()
