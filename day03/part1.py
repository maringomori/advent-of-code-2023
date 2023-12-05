import re

def check_surrounding_indexes(x, y, length, array):
    max_y = len(array)
    max_x = len(array[0])

    for i in range(max(y-1, 0), min(y+2, max_y)):
        for j in range(max(x-1, 0), min(x+length+1, max_x)):
            if i == y and x <= j < x + length:
                continue
            if not (array[i][j].isnumeric() or array[i][j] == "."):
                return i, j 
    return False

input = open("input.txt", "r").read().split("\n")

valid_nums = []
found_symbol_cords = []
for y, line in enumerate(input):
    for match in re.finditer(r'\d+', line):
        x, number = match.start(), match.group()
        if check_surrounding_indexes(x, y, len(number), input):
            valid_nums.append(number)
            

sum = 0
for num in valid_nums:
    sum += int(num)
print("Sum:", sum)

# 32:11
