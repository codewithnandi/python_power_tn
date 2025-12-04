#python dictionaries
my_dict = {
    'Name': 'Alice', 
    'Age': 30, 
    'City': 'New York', 
    'Skills': ['Python', 'Data Analysis', 'Machine Learning']}
D = {
    1: 'One',
    2: 'Two', 
    3: 'Three',
    4: 'Four' ,
    5: 'Five'
}
print("Original Dictionary: ", my_dict)
print("Original Dictionary: ", D)

# accessing disctionary items using key
print("Name: ", my_dict['Name'])
print("Age: ", my_dict['Age'])

# accessing dictionary items using get function
print("City : ",my_dict.get("City"))
print("Skills : ",my_dict.get("Skills"))

# ADDING new key-value pair to the dictionary
my_dict['Profession'] = 'Data Scientist'
print("Updated Dictionary: ", my_dict)

# REMOVING key-value pair from the dictionary
del my_dict['Skills']
print("Removed Value: ", my_dict)

#iterating through the dictionary
for key in my_dict:
    print(key, ":", my_dict[key])   
for key, value in D.items():
    print(key, ":", value)
    
