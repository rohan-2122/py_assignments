# Find Factors
def factors(n):

    factors = []

    i = 1
    while i <= n:
        if n % i == 0:
            factors.append(i)   #i is a factor of n
        i = i + 1

    return factors


n = int(input("Enter a no."))
result  = factors(n)
print(f"The fcators of the number {n} are:  {result}")
