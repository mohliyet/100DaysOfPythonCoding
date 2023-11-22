target = int(input("Enter a number between 0 and 1000:\n")) # Enter a number between 0 and 1000


sum = 0 
for number in range(0,target+1,2):
  sum +=number
print(sum)