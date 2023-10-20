import os
path = 'G:\PythonProjects\File_Handling'

# here  creating  a new directory
def create_dir(dirname):
    os.mkdir(dirname)

# create file inside direcotry
def create_file(dirname, filename):
    os.chdir(dirname)
    with open(filename, "w") as f:
        f.write("I am Karan Tanwar.\nI live in India.")

# append text inside file by this function
def append_file(filename, text):
    with open(filename, "a") as f:
        f.write(text)

# read file by this function      
def read_file(filename):
    with open(filename, "r") as f:
        print(f.read())
        
#delete file by this function
def delete_file(filename):
    os.remove(filename)

# renaming of fine by this function
def rename_file(filename, new_filename):
    os.rename(filename, new_filename)

# here we create file and show 
def give_path_and_filename(dirname, filename):
    with open(filename, "w") as f:
        f.write("I am Karan Tanwar.\nI live in India.")

    print(f"\nContent of {dirname}:")
    print(f"File: The key components of an enterprise levels {filename}\n")



while True:
    
    print("Options:")
    print("1. List files and directories")
    print("2. Create a directory")
    print("3. Delete a file")
    print("4. Rename a file")
    print("5. Exit")
    n = int(input("Enter your choice: "))
    print()

    if n==1:
        create_file(input("Enter dirname: "), input("Enter filename: "))
    
    elif n==2:
        create_dir(input("Enter name of directory: "))

    elif n==3:
        delete_file(input("Enter name of file which you want to delete: "))
    
    elif n==4:
        rename_file(input("Enter current file name: "), input("Enter new name of file: "))
    elif n==5:
        break



