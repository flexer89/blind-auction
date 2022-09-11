import functions

print(functions.logo)
auctions_data = {}
other_users = "yes"

while other_users == "yes":
  functions.clear()
  name = input("Give me your name: ")
  bid = int(input("Give me your bid: "))
            
  auctions_data[name] = bid
  other_users = input("If there are other users who want to bid? ").lower()
functions.find_winner(auctions_data)
