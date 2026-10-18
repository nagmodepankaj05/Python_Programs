n = int(input("Enter Range : "))

even = []
odd = []
for i in range(1,n+1):
    if i%2==0:
        even.append(i)
    else : 
        odd.append(i)


even_num = " ".join(map(str, even))
odd_num = " ".join(map(str,odd))

print("Even Numbers : ", even_num)
print("Odd Numbers : ", odd_num)