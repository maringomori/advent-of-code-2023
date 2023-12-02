input = open("input.txt", "r").read().split("\n")

power_sum = 0
for game in input:
    sets = game.split(": ")[1].split("; ")
    is_game_valid = True

    game_max_color_amount = {
        "red": 1,
        "green": 1,
        "blue": 1,
    }

    for set in sets:
        for i in set.split(", "):
            amount, color = i.split(" ")
            if int(amount) > game_max_color_amount[color]:
                game_max_color_amount[color] = int(amount)
    power_sum += game_max_color_amount["red"] * game_max_color_amount["green"] * game_max_color_amount["blue"]
        
print("solution: " + str(power_sum))

# 8:30
# Total time 23:46