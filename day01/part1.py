input = open("input.txt", "r").read().split("\n")

values = []
for i in input:
    print(i)
    current = ""
    for j in i:
        try:
            int(j)
            current += j
        except:
            pass
    values.append(current)

final_values = []
for i in values:
    if len(i) == 1 or len(i) == 0:
        final_values.append(i + i)

    elif len(i) > 1:
        final_values.append(i[0]+i[-1])

sum = 0
for i in final_values:
    sum += int(i)
print("Solution:")
print(sum)

# 9:53
