n = int(input("Enter number to check : "))

rev =0
num = n

while n >0 :
    digit = n%10
    rev = rev *10 + digit
    n //= 10

if num == rev:
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")

