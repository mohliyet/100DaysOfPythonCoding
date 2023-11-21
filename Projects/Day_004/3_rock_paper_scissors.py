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

import random
#Write your code below this line 👇
input_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if input_number == 0:
    print(rock)
elif input_number == 1:
    print(paper)
elif input_number == 2:
    print(scissors)
else:
    pass

print('Computer chose:')
computer_choose = random.randint(0,2)
print(computer_choose)
if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose == 2:
    print(scissors)
else:
    pass

if (input_number == 0 and computer_choose == 2) or (input_number == 2 and computer_choose == 1) or (input_number == 1 and computer_choose == 0):
    print('You won!')
elif (input_number == 0 and computer_choose == 0) or (input_number == 1 and computer_choose == 1) or (input_number == 2 and computer_choose == 2):
    print('Draw!')
elif input_number>=3:
    print("You entered an invalid number!")
else:
    print('You lose!')




