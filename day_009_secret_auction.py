logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

import os

# Function to clear the terminal screen 
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Create empty dictionary
bidding = {}

# Function to determine the highest bidder using the 'bid_log' parameter inside of the function
def highest_bidder(bid_log):
    high_bid = 0
    high_bidder = ''
    for bidder in bid_log:
        bid = bid_log[bidder]
        if bid > high_bid:
            high_bid = bid
            high_bidder = bidder
    print(f'Congratulations {high_bidder}!! You just won the prize with your bid being the highest at: ${high_bid}')

# Loops through the prompts for bidders, and adds them to the dictionary
more_bidders = 'yes'
while more_bidders == 'yes':
    bidder_name = input('Please enter your name: ')
    bid_amount = int(input('Please enter your bid price in USD: $'))
    # Adds the key (bidder_name) and its corresponding value (bid_amount) to the dictionary to be used
    bidding[bidder_name] = bid_amount
    more_bidders = input('Are there any other bidders that must enter their bids? Please enter "yes" or "no": ').lower()
    if more_bidders == 'yes':
        clear()

highest_bidder(bidding)


