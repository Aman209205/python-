import random
"""
1 for rock
-1 for paper 
0 for scissors 
"""
computer = random.choice([-1,0,1])
youstr = input("Enter your choise: ")
youDict = {"r":1, "p":-1, "s": 0}
reverseDict = {1:"rock", -1:"paper", 0:"scissors"}
you = youDict[youstr]
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if (computer == you ):
    print("It's draw!")

elif (computer==1 and you == 0):
    print("You loose!")

elif (computer ==1 and you == -1):
    print("You loose!")

elif (computer==0 and you==1):
    print("You won!")

elif (computer==0 and you ==-1):
    print("You loose!")

elif (computer==-1 and you == 1):
    print("You won!")

elif (computer==-1 and you ==0):
    print("You won!")

else:
    print ("something went wrong!")
