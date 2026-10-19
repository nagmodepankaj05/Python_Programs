n = int(input("Enter number to count digit : "))
num = n
count = 0

while n > 0:
    count += 1
    n //= 10  #separate last digit 123 => 12, 12=> 1

print(f"Count of {num} : {count}")