input = open("input.txt", "r").read().split("\n")

sum_points = 0
for i in input:
    w, n = i.split(":")[1].split("|")
    winning_numbers = w.strip().split(" ")
    numbers = n.strip().split(" ")

    # Convert list items to ints pass the element if it's not a number
    winning_numbers = [int(i) for i in winning_numbers if i.isdigit()]
    numbers = [int(i) for i in numbers if i.isdigit()]

    

    
    points = 0

    for number in numbers:
        if number in winning_numbers:
            if points == 0:
                points += 1
            else: 
                points *= 2

    sum_points += points

print(sum_points)

#13:44