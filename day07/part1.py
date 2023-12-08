input = open("input.txt", "r").readlines()


def analize_hand(hand):
    winning_orders = ["five", "four", "fullhouse", "three", "two", "one"]
    
    hand_dict = {}
    for i in hand:
        hand_dict[i] = hand.count(i)
    
    of_a_kind = []
    for k, v in hand_dict.items():
        if v == 5:
            of_a_kind.append("five")
        if v == 4:
            of_a_kind.append("four")
        if v == 3:
            of_a_kind.append("three")
        if v == 2:
            of_a_kind.append("two")
        if v == 1:
            of_a_kind.append("one")

    
    if "three" in of_a_kind and "two" in of_a_kind:
        return "fullhouse"

    if len(of_a_kind) == of_a_kind.count("one"):
        return "nopair"
    if of_a_kind.count("two") == 2:
        return "two"
    elif of_a_kind.count("two") == 1:
        return "one"
    

    order = {key: i for i, key in enumerate(winning_orders)}

    sorted_data = sorted(of_a_kind, key=lambda x: order.get(x, len(winning_orders)))
    return sorted_data[0]



winning_orders = ["five", "four", "fullhouse", "three", "two", "one"]

cards_order = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

hands_to_bids = {} 

for i in input:
    hands_to_bids[i.split(" ")[0]] = int(i.split(" ")[1])


winnings = {
    "five": [],
    "four": [],
    "fullhouse": [],
    "three": [],
    "two": [],
    "one": [],
    "nopair": []
}
for k, v in hands_to_bids.items():
    winnings[analize_hand(k)].append({k:v})


ranks = []
for k, v in winnings.items():
    if len(v) > 1:
        same_type_rank_order = []
        for hand in v:
            for l, w in hand.items():
                hand_ranks = [cards_order[card] for card in l]
                same_type_rank_order.append((hand_ranks, l, w))


        same_type_rank_order.sort(key=lambda x: x[0])

        current_type = []
        for hand_rank, original_l, original_w in same_type_rank_order:
           current_type.append({original_l: original_w})
        
        ranks.append({ k: current_type})
    else: 
        ranks.append({k:v})

ranks.reverse()
print(ranks)

total_winnings = 0
rank_number = 1
for i in ranks:
    for k, v in i.items():     
        for j in v:
            for l, w in j.items():
                total_winnings += (w * rank_number)
                rank_number += 1

print(total_winnings)

# 1:19:39