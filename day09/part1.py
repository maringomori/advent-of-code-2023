input = open("input.txt", "r").readlines()

def generate_next_row(row):
    new_row = []
    for i in range(len(row)-1, 0, -1):
        new_row.append(row[i] - row[i-1])

    new_row.reverse()
    return new_row

def calculate_next_value(row, pev_row):
    return row[-1] + pev_row[-1]

sum = 0
for i in input:
    history = []
    history.append([int(num) for num in i.strip().split(" ")])
    
    index = 0
    while not len(history[-1]) == history[-1].count(0):
        history.append(generate_next_row(history[index]))
        index += 1
    
    for j in range(len(history)-1, 0, -1):
        history[j-1].append(calculate_next_value(history[j], history[j-1]))

    sum += history[0][-1]

print(sum)

# 21:12