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

#extending a list by adding more elements
my_list.extend(['New Element', 55, 75.25])
print("Extended List: ", my_list) 
#shorting the list in ascending order
num_list = [45, 12, 78, 23, 56] 
print("number List before sorting: ", num_list)
shorting = sorted(num_list)
print("number List after sorting: ", shorting)
#reversing the list
reversed_list = list(reversed(num_list))
print("Reversed List: ", reversed_list)