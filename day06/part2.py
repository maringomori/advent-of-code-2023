input = open("input.txt", "r").readlines()

# get only the numbers from the list

times = [int(i) for i in input[0].split(":")[1].strip().split(" ") if i.isnumeric()]
distances = [int(i) for i in input[1].split(":")[1].strip().split(" ") if i.isnumeric()]

times = [int(''.join(str(num) for num in times))]
distances = [int(''.join(str(num) for num in distances))]

def calculate_distance(hold_down_time, time):
    return (time-hold_down_time) * hold_down_time

total_wins = 0
for i in range(len(times)):

    won_n_times = 0 
    for j in range(times[i]):
        if distances[i] < calculate_distance(j, times[i]):
            won_n_times += 1

    if total_wins == 0:
        total_wins += won_n_times
    else:
        total_wins *= won_n_times


print(total_wins)
# 2:20