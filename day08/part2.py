from concurrent.futures import ThreadPoolExecutor
from math import lcm

input = open("input.txt", "r").readlines()

directions = [i for i in input[0].strip()]

{
    "AAA": {
            "L": { "CCC" },
            "R": { "BBB" },
          },
}

map_dict = {}
map = input[2:]
for i in map:
    start, tos = i.strip().split(" = ")
    tos = tos.split(", ")
    left = tos[0][1:]
    right = tos[1][0:-1]
    map_dict[start] = {
        "L": left,
        "R": right,
    }

starting_positions = []
for i in map_dict.keys():
    if i[-1] == "A":
        starting_positions.append(i)



""" TOO SLOOOOOOW
counter = 0
step = 0
all_ends_on_z = False
while not all_ends_on_z:
    for i in range(len(starting_positions)):
        starting_positions[i] = map_dict[starting_positions[i]][directions[step]] 

    counter += 1
    step += 1
    if len(directions) == step:
        step = 0
    
    for i in starting_positions:
        if i[-1] == "Z":
            all_ends_on_z = True
        else:
            all_ends_on_z = False
            break
"""
"""
while not all_ends_on_z:
    for i in range(len(starting_positions)):
        starting_positions[i] = map_dict[starting_positions[i]][directions[step]] 

    counter += 1
    step += 1
    if len(directions) == step:
        step = 0
    
    for i in starting_positions:
        if i[-1] == "Z":
            all_ends_on_z = True
        else:
            all_ends_on_z = False
            break
"""

counters = []
for i in starting_positions:
    counter = 0
    step = 0
    while i[-1] != "Z":
        i = map_dict[i][directions[step]] 
        step += 1
        counter += 1
        if len(directions) == step:
            step = 0

    counters.append(counter)

print(lcm(*counters))


#34:19