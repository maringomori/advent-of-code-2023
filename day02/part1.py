input = open("input.txt", "r").read().split("\n")


colors_amount = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
id = 1
valid_games_sum = 0
for game in input:
    sets = game.split(": ")[1].split("; ")
    is_game_valid = True
    for set in sets:
        for i in set.split(", "):
            amount, color = i.split(" ")
            if int(amount) > colors_amount[color]:
                is_game_valid = False
                break
    if is_game_valid:   
        valid_games_sum += id
        
    id += 1

print("Solution: " + str(valid_games_sum))

# 15:16