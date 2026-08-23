# Silent Auction Project
import art

print(art.logo)

auction_bids = {}
additional_bids = True

while additional_bids:

    bidder_name = input("What is your name? ")
    bet_amount = int(input("How much do you bet? "))


    auction_bids[bidder_name] = bet_amount
    additional_bets = input("Are there additional bids? y for yes and n for no: ")
    if additional_bets == "n":
        additional_bids = False
        highest_bid = 0
        for bid in auction_bids:
            if auction_bids[bid] > highest_bid:
                print(f"{bid} won the bid with ${auction_bids[bid]}")


    elif additional_bets == "y":
        print(100 * "\n")
