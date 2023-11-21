line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
if position[0] =='A':
  index_0 = 0
if position[0]=='B':
  index_0 = 1
if position[0]=='C':
  index_0 = 2
index_1 = int(position[1])

if index_1==1:
  line1[index_0] = 'X'
elif index_1==2:
  line2[index_0] = 'X'
else:
  line3[index_0] = 'X'
print(f"{line1}\n{line2}\n{line3}")