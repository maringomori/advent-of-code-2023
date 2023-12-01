def replace_to_numbers(file):
    output = []
    for i in file:
        # replace numbers as words to numbers   
        i = i.replace("one", "one1one")
        i = i.replace("two", "two2two")
        i = i.replace("three", "three3three")
        i = i.replace("four", "four4four")
        i = i.replace("five", "five5five")
        i = i.replace("six", "six6six")
        i = i.replace("seven", "seven7seven")
        i = i.replace("eight", "eight8eight")
        i = i.replace("nine", "nine9nine")
        i = i.replace("zero", "zero0zero")
        output.append(i)
        
    return output
input = open("input.txt", "r").read().split("\n")

input = replace_to_numbers(input)

values = []
for i in input:

    current = ""
    print(i)

    for j in i:
        try:
            int(j)
            current += j
        except:
            pass
    print(current)
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

#Part2: 21:24
#Total: 31:17
