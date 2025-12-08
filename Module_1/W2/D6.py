# # CSV file handling
import csv
path = "Module_1/W2/assets/"

# # writing into csv file
# # with open(path+"employee.csv", 'w', newline='') as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["id", "name", "department", "salary"])
# #     writer.writerow(["1", "Tripan", "HR", 50000])
# #     writer.writerow(["2", "Neha", "Engineering", 60000])
# #     writer.writerow(["3", "Debopriya", "Marketing", 45000])
# #     writer.writerow(["4", "Suvendu", "Marketing", 55000])

# # reading from csv file
# with open(path+"employee.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"Row: {row}")

# # using DictReader to read from CSV
with open (path+"employee.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"ID: {row['id']}, Name: {row['name']}, Department: {row['department']}")

#writing dictionary to csv 
print("-------- Writing Dictionary to CSV -------")
employees = [
    {'Name': 'Tripan', 'Age': 30, 'Department': 'HR', 'Salary': 50000},
    {'Name': 'Neha', 'Age': 28, 'Department': 'Engineering', 'Salary': 60000},
    {'Name': 'Debopriya', 'Age': 35, 'Department': 'Marketing', 'Salary': 45000},
    {'Name': 'Suvendu', 'Age': 32, 'Department': 'Marketing', 'Salary': 55000}
]
with open(path+"employee_dict.csv", 'w', newline='') as new_file:
    fieldNames = ['Name', 'Age', 'Department', 'Salary']
    writer = csv.DictWriter(new_file, fieldnames = fieldNames)
    writer.writeheader()
    writer.writerows(employees)
    