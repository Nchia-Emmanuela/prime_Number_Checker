def prime_checker(number):
    is_prime = True
    for i in range(2, number -1):
        if number / i == 0:
            is_prime = False
    if is_prime:
        print("It's a Prime Number")
    else:
        print("It's not a Prime NUmber")
    
n = int(input("Check this number: \n"))
prime_checker(number =  n)

            


    