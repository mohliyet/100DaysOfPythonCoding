from art import logo
import os
print(logo)
print("Welcome to hte secret auction program.")


bidders = []

bidder_avaliable = True

while bidder_avaliable:
    name = input('What is your name?: ')
    bid_value = int(input("What is your bid?: $"))
    temp = {
         "name": name,
         "bid_value": bid_value
         }
    bidders.append(temp)
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if next_bidder=='no':
        bidder_avaliable=False
    os.system("cls")

bid_value_ = 0    
for bidder in bidders:
    if bidder['bid_value'] > bid_value_:
        name_ = bidder['name']
        bid_value_ = bidder['bid_value']

print(f'The winner is {name_} with a bid of ${bid_value_}')


# os.system("cls")
