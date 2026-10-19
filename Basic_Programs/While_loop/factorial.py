n = int(input("Enter number for factorial : "))

fact = 1
i=1

while i <= n:
    fact = fact * i
    i+=1

print(f"Factorial of {n} : {fact}")