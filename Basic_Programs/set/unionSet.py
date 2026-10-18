A = {12,32,34,5,65}
B = {32,3,34,51,33}

C = A.union(B) #also used A | B

print("Union : " , C)

D = A.intersection(B) #Also used A&B
print("Intersection : " , D)

E = A.difference(B) #also use A - B. Remember A - B and B - A

print("Difference : ", E)

F = A.symmetric_difference(B) #also use A ^ B

print("Symmetric Difference:", F)