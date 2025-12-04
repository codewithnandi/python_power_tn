# creation of object of file
path = "Module_1/W2/assets/"
file = open(path+"example.txt ",'r')

# reading entire file
#content = file.read()
#print("Entire Content : ", content)

# reading first 100 charachter
#first_100_chars = file.read(150)
#print("First 100 char of file : ", first_100_chars)

# reading line by line
#line1 = file.readline()
#line2 = file.readline()
#print(f"Line 1 : {line1})")
#print(f"Line 2 : {line2})")

#reading all lines into a list
all_lines = file.readlines()
print(f"total lines:  {len(all_lines)}")
for line in all_lines:
    print(f"line: {line.strip()}")


#itarateing through file object
for line in file:
    print(f"line: {line.strip()}")

file.close()
