#writeing to files
path = "Module_1/W2/assets/"
file = open(path+"output.txt",'w')
# file.write("hello world\n")
# file.write("tripan, student of bca") 

#write a list of strings
# lines = ["first line\n", "second line\n", "third line\n"]
# file.writelines(lines)

# appending data without overwriting
file.write("\nappending new line at the end of file")


file.close()   
