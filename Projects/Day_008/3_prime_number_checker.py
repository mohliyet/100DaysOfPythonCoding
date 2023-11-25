# def prime_checker(number):
#   cnt = 0
#   for i in range(1,number+1):
    # if number%i == 0:
    #   cnt+=1
#   if cnt==2:
    # print("It's a prime number.")
#   else:
    # print("It's not a prime number.")

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number%i==0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input('Write a number: '))
prime_checker(number=n)