def add_bid(person, amt, bid_list):
    """
    This function adds a new entry into the appropriate dictionary
    :param person: the name of the bidder
    :param amt: their bid amount
    :param bid_list: the dictionary in which the bidder and bid will be stored in
    :return:
    """
    bid_list[person] = amt


def winner(bid_list):
    """
    This function will determine the highest bidder and print to screen who it is and wht their winning bid was
    :param bid_list: the dictionary that has all the bidders and their bids
    :return:
    """
    winner_name = ''
    winner_bid = 0

    for bid in bid_list:
        if bid_list[bid] > winner_bid:
            winner_name = bid
            winner_bid = bid_list[bid]

    print(f"The winner of this silent auction is {winner_name} with a bid amount of ${winner_bid}")




