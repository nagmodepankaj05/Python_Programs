A = (10, 20, 30, 40, 50)

num = int(input("Enter number: "))

if num in A:
    print("Index:", A.index(num))
else:
    print("Element not found")