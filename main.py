from replit import clear


from art import logo
print(logo)

continuation_of_auction = True

while continuation_of_auction == True:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: $"))

  bidders = {}
  bidders[name] = bid

  continuation = input("Are there other players left type 'yes' if so. Otherwise, 'no'\n")

  if continuation == 'no':
    continuation_of_auction = False
  else:
    clear()
    continuation_of_auction == True

max_bidder = max(bidders, key=bidders.get)
print(f"The winner of the auction is {max_bidder}")