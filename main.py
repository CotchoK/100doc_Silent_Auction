# Import modules
import os  # used to import the clear screen functionality
import functions as f  # import program specific functions
import ascii_art as aa # import ascii art file

# define the clear terminal screen function
# note ensure to check the Emulate Terminal in Output Console in the Configurations settings
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# print the gavel
print(aa.logo)

# print intro text
print("Welcome to the secret auction program.")

# declare variables
name = ''
bid = 0
bidders = {}
finished = False # used to keep while loop going whenever a user says 'yes' to another bidder

# while loop to keep the program functioning until a 'no' command is entered
while not finished:
    # ask user for name and bid amount
    name = input("What is your name? ")
    bid = int(input("Please enter your bid $"))

    # add bid to the bidders dictionary
    f.add_bid(person=name, amt=bid, bid_list=bidders)

    # ask the user if there is another bidder
    response = input("Is there another bidder? 'yes' or 'no'? ")

    # if response is no then clear the screen and exit while loop
    if response == 'no':
        cls()
        finished = True
    # else just clear the screen and loop from the top of the while loop again
    else:
        cls()

# finally calculate who the winner is
f.winner(bid_list=bidders)
