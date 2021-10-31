from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
auction_list = {}



any_more = 'yes'

while any_more == 'yes':

 clear()
 
 print(logo)
 print("welcome to the auction")

 name  = input("what is the name of the bidder: ")
 price = input("what is the bid price: ")

 auction_list[name] = price

 any_more = input("Are there any more Bidders? type yes or no ").lower()
 
#find the highes bidder
clear()

max_bidder = max(auction_list,key=auction_list.get)

print(f"The maximum bidder is {max_bidder} and bid price is "\
      f"{auction_list[max_bidder]}")
  
   
