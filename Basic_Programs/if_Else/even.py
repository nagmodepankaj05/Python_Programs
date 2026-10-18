n = int(input("Enter range : "))
even = []
for i in range(1,n):
    if i%2==0:
        even.append(i)


evenNum = " ".join(map(str, even))

print("Even numbers : ", evenNum)