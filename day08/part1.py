input = open("input.txt", "r").readlines()

print(input)
directions = [i for i in input[0].strip()]

{
    "AAA": {
            "L": { "CCC" },
            "R": { "BBB" },
          },
}

map_dict = {}
map = input[2:]
print(map)
for i in map:
    start, tos = i.strip().split(" = ")
    tos = tos.split(", ")
    left = tos[0][1:]
    right = tos[1][0:-1]
    map_dict[start] = {
        "L": left,
        "R": right,
    }

current_position = "AAA"
counter = 0
step = 0
while current_position != "ZZZ":
    current_position = map_dict[current_position][directions[step]] 
    step += 1
    counter += 1
    if len(directions) == step:
        step = 0

print(counter)

#15:55