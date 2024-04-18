def add_bid(person, amt, bid_list):
    bid_list[person] = amt


def winner(bid_list):
    winner_name = ''
    winner_bid = 0

    for bid in bid_list:
        if bid_list[bid] > winner_bid:
            winner_name = bid
            winner_bid = bid_list[bid]

    print(f"The winner of this silent auction is {winner_name} with a bid amount of ${winner_bid}")




