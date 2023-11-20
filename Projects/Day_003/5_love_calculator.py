print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

T = (name1+name2).lower().count('t')
R = (name1+name2).lower().count('r')
U = (name1+name2).lower().count('u')
E = (name1+name2).lower().count('e')

TRUE = T+R+U+E

L = (name1+name2).lower().count('l')
O = (name1+name2).lower().count('o')
V = (name1+name2).lower().count('v')
E = (name1+name2).lower().count('e')

LOVE = L+O+V+E
love_score = int(str(TRUE)+str(LOVE))

if love_score < 10 or love_score > 90:
  print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score > 40 and love_score < 50:
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f'Your score is {love_score}.')

