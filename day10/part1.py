import math
import sys
sys.setrecursionlimit(99999)
input = open("input.txt", "r").readlines()

def find_starting_pos(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "S":
                return [i, j]

"""
scrap this
def find_next_step(distances, current_distance, input, current_pos):
    current_pos_char = input[current_pos[0]][current_pos[1]] 
    distances[current_pos[0]][current_pos[1]] = current_distance

    | is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
    if current_pos_char == "|":
        if distances[current_pos[0]+1][current_pos[1]] > distances[current_pos[0]-1][current_pos[1]]:
            if input[current_pos[0]+1][current_pos[1]] == "S":
                current_pos[0] -= 1
            else:
                current_pos[0] += 1
        else:
            if input[current_pos[0]-1][current_pos[1]] == "S":
                current_pos[0] += 1
            else:
                current_pos[0] -= 1

    elif current_pos_char == "-":
        if distances[current_pos[0]][current_pos[1]+1] > distances[current_pos[0]][current_pos[1]-1] or input[current_pos[0]][current_pos[1]+1] == "S":
            current_pos[1] += 1
        else:
            current_pos[1] -= 1
    elif current_pos_char == "L":
        current_pos[0] -= 1
    elif current_pos_char == "J":
        current_pos[1] -= 1
    elif current_pos_char == "7":
        current_pos[0] += 1
    elif current_pos_char == "F":
        current_pos[1] += 1  
    elif current_pos_char == ".":
        pass
    elif current_pos_char == "S":
        print("Found exit!")
        return
    next_pos_char = input[current_pos[0]][current_pos[1]]
    print(next_pos_char)
    current_distance += 1
    find_next_step(distances, current_distance, input, current_pos)
"""


"""scrap this
def find_next_step(input, steps):

    current_pos = steps[-1]
    current_pos_char = input[current_pos[0]][current_pos[1]]
    with open("output.txt", "a") as f:
        f.write(current_pos_char + " " + str(current_pos[0]) +" " +str(current_pos[1]) + "\n")

    next_step = []
    if current_pos_char == "-":
        if [current_pos[0], current_pos[1]-1] == steps[-2]:
            next_step = [current_pos[0], current_pos[1] + 1] 
        else:  
            next_step = [current_pos[0], current_pos[1] - 1]
    elif current_pos_char == "|":
        if [current_pos[0]-1, current_pos[1]] == steps[-2]:
            next_step = [current_pos[0]+1, current_pos[1]]
        else:
            next_step = [current_pos[0]-1, current_pos[1]]
    elif current_pos_char == "L":
        if [current_pos[0]+1, current_pos[1]] == steps[-2]:
            next_step = [current_pos[0]+1, current_pos[1]]
        else:
            if [current_pos[0]-1, current_pos[1]] == steps[-2]:
                next_step = [current_pos[0], current_pos[1]+1]
            else:
                next_step = [current_pos[0]-1, current_pos[1]]
    elif current_pos_char == "J":
        if [current_pos[0]+1, current_pos[1]] == steps[-2]:
            next_step = [current_pos[0]-1, current_pos[1]]
        else:
            if [current_pos[0], current_pos[1]-1] == steps[-2]:
                next_step = [current_pos[0]-1, current_pos[1]]
            else:
                next_step = [current_pos[0], current_pos[1]-1]
    elif current_pos_char == "7":

        if [current_pos[0], current_pos[1]] == steps[-2]:
            next_step = [current_pos[0], current_pos[1]+1]
        else:
            next_step = [current_pos[0]+1, current_pos[1]]
    elif current_pos_char == "F":
        if [current_pos[0]-1, current_pos[1]] == steps[-2]:
            next_step = [current_pos[0]+1, current_pos[1]]
        else:
            if [current_pos[0]+1, current_pos[1]] == steps[-2]:
                next_step = [current_pos[0], current_pos[1]+1]
            else:
                next_step = [current_pos[0], current_pos[1]-1]
    elif current_pos_char == ".":
        pass
    elif current_pos_char == "S":
        print("Found exit!")
        return
    

    steps.append(next_step)
    find_next_step(input, steps)
"""


input = [i.strip() for i in input]
print(input)

distances = [[math.inf for i in range(len(input[0]))] for j in range(len(input))]

start_pos = find_starting_pos(input)

def find_next_step(input, steps, relative_pos_to_char):
    current_pos = steps[-1]
    prev_pos = steps[-2]
    current_pos_char = input[current_pos[0]][current_pos[1]]
    """
    with open("output.txt", "a") as f:
        f.write(current_pos_char + " " + str(current_pos[0]) +" " +str(current_pos[1]) + "\n")
    """
    next_step = []
    relative_pos_to_char[current_pos_char]
    
    if current_pos_char == ".":
        return None
    
    if current_pos_char == "S":
        return steps
    
    if prev_pos == [current_pos[0] + relative_pos_to_char[current_pos_char][0][0], current_pos[1] + relative_pos_to_char[current_pos_char][0][1]]:
        next_step = [current_pos[0] + relative_pos_to_char[current_pos_char][1][0], current_pos[1] + relative_pos_to_char[current_pos_char][1][1]]
    else:  
        next_step = [current_pos[0] + relative_pos_to_char[current_pos_char][0][0], current_pos[1] + relative_pos_to_char[current_pos_char][0][1]]
    
    steps.append(next_step)
    return find_next_step(input, steps, relative_pos_to_char)

relative_pos_to_char = {
    "|" : [[1, 0], [-1, 0]],
    "-" : [[0, 1], [0, -1]],
    "L" : [[-1, 0], [0, 1]],
    "J" : [[-1, 0], [0, -1]],
    "7" : [[1, 0], [0, -1]],
    "F" : [[1, 0], [0, 1]],
    "." : [],
    "S" : []
}
#steps= [start_pos, [start_pos[0], start_pos[1]+1]]

circles = []

steps = [start_pos, [start_pos[0]+1, start_pos[1]]]
circle_steps = find_next_step(input, steps, relative_pos_to_char)
if circle_steps != None:
    circles.append(circle_steps)

steps = [start_pos, [start_pos[0]-1, start_pos[1]]]
circle_steps = find_next_step(input, steps, relative_pos_to_char)
if circle_steps != None:
    circles.append(circle_steps)

steps = [start_pos, [start_pos[0], start_pos[1]+1]]
circle_steps = find_next_step(input, steps, relative_pos_to_char)
if circle_steps != None:
    circles.append(circle_steps)
    
steps = [start_pos, [start_pos[0], start_pos[1]-1]]
circle_steps = find_next_step(input, steps, relative_pos_to_char)
if circle_steps != None:
    circles.append(circle_steps)

max_distance = 0
print(circles)
for i in circles:
    current_distance = int(len(i)/2)
    if current_distance > max_distance:
        max_distance = current_distance
print(max_distance)

# 2:24:23