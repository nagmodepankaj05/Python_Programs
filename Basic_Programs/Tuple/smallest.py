A = (10, 25, 5, 40, 15)

smallest = A[0]

for i in A:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)