n = int(input("Enter Range of Fibo : "))

fibo = []
fibo.append(0)
fibo.append(1)
for i in range(2, n):
    new = fibo[i-2] + fibo[i-1]
    fibo.append(new)

print(fibo)