#python tuples 
T=(20, 'Python Power', 35.75, [20, 40, 60])
print("Original Tuple: ", T)

# traversing through the elements of the TUPLE
for i in range(0, len(T)):
    print(T[i])

#slicing in tuple
#syntax: tuple_name[start_index:end_index]
tup =  ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango", "Pineapple")

print("Sliced Tuple: ", tup[1:4])  
print("Sliced Tuple from index 2 to end: ", tup[2:])      
print("Sliced Tuple from start to index 3: ", tup[:3])
print("Sliced Tuple with negative indices: ", tup[-4:-1])  
print("Sliced Tuple with step: ", tup[::2])  
print("Sliced Tuple with reverse: ", tup[::-1])  
print("Sliced Tuple with start, end and step: ", tup[1:5:2])

#maximum and minimum in tuple
num_tuple = (45, 12, 78, 23, 56, 78, 90, 11)
print("Maximum value in tuple: ", max(num_tuple))
print("Minimum value in tuple: ", min(num_tuple))
print("count of the tuple: ", len(num_tuple))
print("Count the occurance of 78: ", num_tuple.count(78))
