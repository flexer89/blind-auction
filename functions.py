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
def clear():
  print("\033[H\033[J", end="")

def find_winner(auctions_data):
  max_bid = 0
  winner = ""
  for bidder in auctions_data:
    if auctions_data[bidder] > max_bid:
      max_bid = auctions_data[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${max_bid}")
