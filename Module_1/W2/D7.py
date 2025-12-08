#Error handling while working with any files
# 1. file not found error handling
# 2. permission error handling
# 3. isADirectory error handling
# 4. ioError handling 

#basic tr-y except block
# try:
#     file =open("nonexitingfile.txt", 'r')
#     content = file.read()
#     file.close()
# except FileNotFoundError:
#     print("file not found ")
# except PermissionError:
#     print("No permission to read ")
# except IsADirectoryError:
#     print(f"unexpected error occured: {e}")

#complete try except else finally 

# try:
#     file = open('data.txt', 'r')
#     content = file.read()
# except FileNotFoundError:
#     print("file not found, creating a new file")
#     file = open('data.txt', 'w')
#     file.write("Default content")
#     content = "lorem ipsum dolor sit amet"
# except IOError as e:
#     print()
#     print(f"An I/O error occurred: {e}")
# else:
#     print("File read successfully")
#     print(f"File content length: {len(content)}")
# finally:
#     if 'file' in locals() and not file.closed:
#         file.close()
#     print("Cleanup completed.")

#useing with statement with error handling

try:
    with open('data.txt', 'r') as file:
        content = file.read()
        result = 10 / 0  # This will raise a ZeroDivisionError
except FileNotFoundError:
    print("file not found, creating a new file")
except ZeroDivisionError:
    print("division by zero error occurred")
except IOError as e:
    print(f"An I/O error occurred: {e}")
else:
    print("File read successfully")
     