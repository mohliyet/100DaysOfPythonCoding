def paint_calc(height, width, cover):
  no_of_cans = (height*width)/cover
  if no_of_cans > round(no_of_cans):
    print(f"You'll need {round(no_of_cans)+1} cans of paint.")
  else:
    print(f"You'll need {round(no_of_cans)} cans of paint.")
test_h = int(input("Height: ")) # Height of wall (m)
test_w = int(input("Width: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
