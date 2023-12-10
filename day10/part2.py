import math
import sys
import os

sys.setrecursionlimit(999999999)
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

def flood_fill(matrix, x, y, fill_char, wall_char):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            continue
        if matrix[x][y] == wall_char or matrix[x][y] == fill_char:
            continue

        matrix[x][y] = fill_char

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))

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

print(input)
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


print(circles)


new_input = [[" " for j in range(len(input[0]*3))] for i in range(len(input)*3)]
print(new_input)
print(len(new_input))

for circle in circles:
    for i in range(len(input)):
        new_line = []
        for j in range(len(input[i])):
            if [i, j] in circle:
                if input[i][j] == "-":
                    new_input[i*3+1][j*3] = "█"
                    new_input[i*3+1][j*3+1] = "█"
                    new_input[i*3+1][j*3+2] = "█"
                if input[i][j] == "|":
                    new_input[i*3][j*3+1] = "█"
                    new_input[i*3+1][j*3+1] = "█"
                    new_input[i*3+2][j*3+1] = "█"
                
                if input[i][j] == "L":
                    new_input[i*3][j*3+1] = "█"
                    new_input[i*3+1][j*3+1] = "█"
                    new_input[i*3+1][j*3+2] = "█"
                
                if input[i][j] == "J":
                    new_input[i*3][j*3+1] = "█"
                    new_input[i*3+1][j*3+1] = "█"
                    new_input[i*3+1][j*3] = "█"
                if input[i][j] == "7":
                    new_input[i*3+1][j*3] = "█"
                    new_input[i*3+1][j*3+1] = "█"
                    new_input[i*3+2][j*3+1] = "█"
                if input[i][j] == "F":
                    new_input[i*3+1][j*3+1] = "█"
                    new_input[i*3+1][j*3+2] = "█"
                    new_input[i*3+2][j*3+1] = "█"
                if input[i][j] == "S":
                    for k in range(3):
                        for l in range(3):
                            new_input[i*3+k][j*3+l] = "█"
            else:  
                new_input[i*3+1][j*3+1] = "."
                
            if input[i][j] == ".":
                new_input[i*3+1][j*3+1] = "."

flood_fill(new_input, 0, 0, '@', '█')

with open('output.txt', 'w') as file:
    for i in new_input:
        for j in i:
            file.write(j)  # Write each character to the file
        file.write('\n')  # Add a newline after each inner loop

counter = 0
for i in range(len(new_input)):
    for j in range(len(new_input[i])):
        if new_input[i][j] == ".":
            counter += 1

print(counter)


# 2:00:20
# + 22:12 replace floodfill