import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.sample(word_list,1)[0]


display=[]
for _ in range(len(chosen_word)):
    display.append('_')

# print(f'Total spaces in the guessed word: {display}')
while '_' in display:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
      for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter in guess:
            display[position] = letter
        else:
            pass
      print(display)
    else:
      break
if '_' not in display:
    print('You won!')
else:
   print('You lost!')