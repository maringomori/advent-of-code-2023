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
        cords = check_surrounding_indexes(x, y, len(number), input)
        if cords:
            valid_nums.append(number)
            found_symbol_cords.append(cords)

print("valid symbols:", found_symbol_cords)

print(valid_nums)
print(found_symbol_cords)

coords_dict = {}

for num, coord in zip(valid_nums, found_symbol_cords):
    if coord in coords_dict:
        coords_dict[coord].append(int(num))
    else:
        coords_dict[coord] = [int(num)]

result = 0
for cords, nums in coords_dict.items():
    if input[cords[0]][cords[1]] == '*' and len(nums) > 1:
        product = 1
        for n in nums:
            product *= n
        
        print("product:", product)
        result += product
    


print(result)

# 32:11

# 43:58 

# 43:58 + 32