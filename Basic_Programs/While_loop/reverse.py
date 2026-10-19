n = int(input("Enter number to reverse : "))
num = n
rev =0 
while n > 0 :
    digit = n%10
    rev = rev *10 +digit
    n //= 10

print(f"Original number {num} : {rev }")