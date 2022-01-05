middle = '''
....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
'''
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
game = [rock, paper, scissors]
a = int(input("What do u choose? 0 for Rock, 1 for Paper and 2 for scissors.\n"))

if a<0 or a>2:
  print(middle)
  raise Exception("You can only choose 0, 1 or 2")
else:
  print("You choose:")
  print(game[a])
 
import random
b = random.randint(0,2)
print("Computer choose:\n")
print(game[b])

if (a == b):
  print("Draw")
elif(a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 0):
  print("You lose.")
else:
  print("You win.")
  