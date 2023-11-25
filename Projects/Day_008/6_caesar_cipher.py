alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caecar(direction, input_text, shift_amount):
  output_text = ""
  for letter in input_text:
    position = alphabet.index(letter)
    if direction == 'encode':
      new_position = position + shift_amount
    else:
      new_position = position - shift_amount
    output_text += alphabet[new_position]
  print(f"The {direction}d text is {output_text}")

caecar(direction=direction, input_text=text, shift_amount=shift)