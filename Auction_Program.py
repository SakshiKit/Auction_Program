from turtle import clear

from art2 import logo

print( logo )
print( "Welcome to the secrete Auction Program" )

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    global winner
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print( f"The winner is {winner} with a bid of ${highest_bid}" )


while not bidding_finished:
    name = (input( "What is your name?" ))
    price = (int( input( "What's your Bid? $" ) ))
    bids[name] = price
    last_step = (input( "Are there any other bidders? Type 'YES' or 'NO' " ))
    if last_step == "NO":
        bidding_finished = True
        find_highest_bidder( bids )
    elif last_step == "YES":
        clear()
