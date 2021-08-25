from replit import clear
import art

bids = {}
def add_bids(name, bid):
  bids[name] = bid

def highest_bid():
  highest_bid = 0
  highest_bidder = ""
  for name in bids:
    if int(bids[name]) >= highest_bid:
      highest_bid = int(bids[name])
      highest_bidder = name

  print(f"The winner is {highest_bid} with a bid of {highest_bidder}")

print(art.logo)

print("Welcome to the secret auction program")

any_bidders = True

while any_bidders:
  name = input("What is your name? ")
  bid = input("What's your bid? ")
  add_bids(name, bid)
  choice = input("Are there any other bidders? 'yes' or 'no'\n")

  if choice == 'no':
    any_bidders = False


  elif choice == 'yes':
    clear()

# print(bids)
