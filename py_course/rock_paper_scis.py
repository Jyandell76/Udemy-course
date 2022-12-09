import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
usr_ = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
com_ran = random.randint(0, 2)
com_ = str(com_ran)
if com_ == "0":
    com_ = rock
    if usr_ == "0":
        usr_ = rock
        print(f"Computer showed {com_}")
        print(f"User showed {usr_}")
        print("Draw Game!")
        
    elif usr_ == "1":
        usr_ = paper        
        print(f"Computer showed {com_}")
        print(f"User showed {usr_}")
        print("You Win!")
        
    elif usr_ == "2":
        usr_ = scissors
        print(f"Computer showed {com_}") 
        print(f"User showed {usr_}")
        print("You Lose!")
        
if com_ == "1":
    com_ = paper
    if usr_ == "0":
        usr_ = rock
        print(f"Computer showed {com_}")
        print(f"User showed {usr_}")
        print("You Lose!")
        
    elif usr_ == "1":
        usr_ = paper        
        print(f"Computer showed {com_} User showed {usr_}")
        print("Draw Game!")
        
    elif usr_ == "2":
        usr_ = scissors
        print(f"Computer showed {com_} User showed {usr_}")
        print("You Win!")
        
if com_ == "2":
    com_ = scissors
    if usr_ == "0":
        usr_ = rock
        print(f"Computer showed {com_} User showed {usr_}")
        print("You Win!")
        
    elif usr_ == "1":
        usr_ = paper        
        print(f"Computer showed {com_} User showed {usr_}")
        print("Draw Lose!")
        
    elif usr_ == "2":
        usr_ = scissors
        print(f"Computer showed {com_} User showed {usr_}")
        print("Draw Game!")
        



       
    
    
    

