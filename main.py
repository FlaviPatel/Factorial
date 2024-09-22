def  findFactorial(n):
     if n == 1:
        return n
     return n * findFactorial(n-1)

x = int(input("Enter the number:"))

if x < 0:
    print(x, "is negative")
elif x == 0:
    print("The Factorail of 0 is 1")
else:
    result = findFactorial(x)
    print(f"The factorial of {x} is {result}")
