# Write your code here 👇
upper_limit = int(input('Enter the max number: \n'))

for number in range(1,upper_limit+1):
  if number%3==0 and number%5 ==0:
    print('FizzBuzz')
  elif number%3 == 0 and number%5 !=0:
    print('Fizz')
  elif number%3 !=0 and number%5 ==0:
    print('Buzz')
  else:
    print(number)