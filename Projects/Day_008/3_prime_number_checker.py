def prime_checker(number):
  cnt = 0
  for i in range(1,number+1):
    if number%i == 0:
      cnt+=1
  if cnt==2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
n = int(input('Write a number: ')) # Check this number
prime_checker(number=n)