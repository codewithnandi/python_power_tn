#Advanced Data Structures
#list

#creating a list that holds different types of data
my_list = [20, 'Python Power', 35.75, [20, 40, 60]]
print(my_list)

# traversing through the elements of the LIST
for i in range(0, len(my_list)):
     print(my_list[i]) 

#test mutable property by updating a value
my_list[2] = 99.99
print(my_list)      