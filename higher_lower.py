
# generate random number 

#IMPORT RANDOM NUMBER

#user randint to random integer

# display logo
#import art

#fetch game data function fetch_game data
# first import game_data 
# read to random entries in the list
#make sure two random numbers are not staticmethod


#the one list with more followers keep it more
#read again


from art import logo,vs
from game_data import data
from random import randint
from replit import clear



def pick_random_num():
  return randint(1,49)

def fetch_game_data(num):
  return data[num]

def who_has_more(count_a,count_b):
   if count_a > count_b:
     return 'a'
   else:
     return 'b'

list_A = []
list_B = []
score = 0
game = True

 
while game:

 if score == 0:
   num_a = pick_random_num()
   num_b = pick_random_num()
   print(num_a,num_b)
   list_A = fetch_game_data(num_a)
   list_B = fetch_game_data(num_b)

 

 clear()

 print(logo)
  
 if score > 0:
   print(f"you are correct, current score {score}")
   if more_followers == 'a':
    num_b = pick_random_num()
    print(num_b)
    list_B = fetch_game_data(num_b)
   else:
    num_a = pick_random_num()
    print(num_a)
    list_A = fetch_game_data(num_a)
 
 print(f"Compare A: {list_A['name']},"\
       f"{list_A['description']} from {list_A['follower_count']}")

 print(vs)


 print(f"Againt B:{list_B['name']},"\
       f"{list_B['description']} from {list_B['follower_count']}")

  

 user_choice = input("Who has more followers a or b ").lower()
  
 more_followers=who_has_more(list_A['follower_count'],list_B['follower_count'])

 if user_choice == more_followers:
   score = score + 1
 else:
   game = False

print(f"You are wrong, your score {score}")

 

 





 

