my_set1= {1,2,3,4,5}
my_list= list(my_set1)
print(my_list[0])
my_set2= {5,6,7,8,9}
print(my_set1 | my_set2)
print(my_set1 & my_set2)
print(my_set1 - my_set2)
my_set1.add(10)
print(my_set1)
my_set2.remove(9)
print(my_set2)
my_set1.discard(8)
print(my_set1)