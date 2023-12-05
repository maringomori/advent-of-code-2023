import time
start_time = time.time()
input = open("input.txt", "r").read().split("\n")


def calculate_points(winning_numbers, numbers):
    points = 0
    for number in numbers:
        if number in winning_numbers:
            points += 1
    return points



def solve(count_copy_of_cards, input, i):
    
    w, n = input[i].split(":")[1].split("|")
    winning_numbers = w.strip().split(" ")
    numbers = n.strip().split(" ")

    winning_numbers = [int(i) for i in winning_numbers if i.isdigit()]
    numbers = [int(i) for i in numbers if i.isdigit()]

    points = calculate_points(winning_numbers, numbers)
    for j in range(i+1, i+points+1):
        count_copy_of_cards[j] = count_copy_of_cards.get(j, 0) + 1
        count_copy_of_cards = solve(count_copy_of_cards, input, j)
    return count_copy_of_cards

count_copy_of_cards = {
}
for  i in range(len(input)):
    count_copy_of_cards[i] = count_copy_of_cards.get(i, 0) + 1
    count_copy_of_cards = solve(count_copy_of_cards, input, i)

print(count_copy_of_cards)
sum = 0 
for k, v in count_copy_of_cards.items():
    sum += v

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))

#31:28