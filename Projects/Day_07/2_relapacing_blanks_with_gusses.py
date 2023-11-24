import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.sample(word_list,1)[0]


display=[]
for i in range(len(chosen_word)):
    display.append('_')

# print(f'Total spaces in the guessed word: {display}')

guess = input("Guess a letter: ").lower()


for index , letter in enumerate(chosen_word):
    if letter in guess:
        display[index] = letter
    else:
        pass
print(display)