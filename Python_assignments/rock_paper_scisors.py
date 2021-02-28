# Rock Paper Scissors is a game in which the computer will choose an element between rock, paper and scissors
# Same thing with the user
# r is greater than scissors which is greater than paper

import random
def play():
        
        print("\t\t\tWelcome to the RPS game!!! \n")
        
        user=input("'r' for Rock, 'p' for Paper and 's' for Scissors \n")
        computer = random.choice(['r','p','s'])
        
        if user==computer:
            print ("It's a tie game !!! ")
            play()
        
        elif (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='r' and computer=='p'):
            print("Yay !!!! You win!\n")
        
        else:
            print("Oups!!! You fail !\n")
            play()
play()