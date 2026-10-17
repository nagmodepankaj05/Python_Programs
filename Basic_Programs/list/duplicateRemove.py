A = [12,12,23,32,23]
B= []

for i in A:
    if i not in B:
        B.append(i)

print(f"Duplicate element list : {A}")
print(f"List after Duplicate REmove : {B}")

