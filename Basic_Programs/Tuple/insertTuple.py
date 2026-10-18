A = (12,23,34,54,6)
print("Tuple before insert : ", A)
my_list = list(A)

my_list.insert(2,233)

my_tuple = tuple(my_list)

print("tuple after insert : " , my_tuple)