# find all the primr no. between 2 to 100

def isPrime(n):
    for i in range(2,101):
        is_prime = True
        for j in  range(2, n):
            if n % j == 0:
                is_prime = False
        
    if(is_prime == True):
        print(f"{n} is a Prime Number.")
    else:
        print(f"{n} is a not a Prime Number.")

isPrime((int(input("Enter a Number: "))))