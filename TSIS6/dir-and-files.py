#1
import os

path = "/path/to/directory"

# List only directories
print("Directories:")
for directory in os.listdir(path):
    if os.path.isdir(os.path.join(path, directory)):
        print(directory)

# List only files
print("Files:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

# List all directories and files
print("All directories and files:")
for item in os.listdir(path):
    print(item)

#2
import os

path = "/path/to/directory"

# Check existence
if not os.path.exists(path):
    print("Path does not exist.")
else:
    print("Path exists.")

# Check readability
if not os.access(path, os.R_OK):
    print("Path is not readable.")
else:
    print("Path is readable.")

# Check writability
if not os.access(path, os.W_OK):
    print("Path is not writable.")
else:
    print("Path is writable.")

# Check executability
if not os.access(path, os.X_OK):
    print("Path is not executable.")
else:
    print("Path is executable.")

#3
import os

path = "/path/to/file.txt"

# Check existence
if not os.path.exists(path):
    print("Path does not exist.")
else:
    print("Path exists.")

# Find filename and directory portion of the path
filename = os.path.basename(path)
directory = os.path.dirname(path)

print("Filename:", filename)
print("Directory:", directory)

#4
with open("file.txt", "r") as file:
    line_count = sum(1 for line in file)

print("Number of lines in the file:", line_count)

#5
my_list = ["apple", "banana", "cherry"]

with open("file.txt", "w") as file:
    for item in my_list:
        file.write("%s\n" % item)

#6
import string

for letter in string.ascii_uppercase:
    filename = letter + ".txt"
    with open(filename, "w") as file:
        file.write("This is file %s" % filename)

#7
with open("file1.txt", "r") as file1:
    with open("file2.txt", "w") as file2:
        for line in file1:
            file2.write(line)
#8
import os

path = "/path/to/file.txt"

# Check existence and access
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("File not found or not writable.")
