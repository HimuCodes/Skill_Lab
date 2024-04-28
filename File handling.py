# Write python program to understand different File handling operations
import os

# Function to create a new file
def create_file(file_name):
    with open(file_name, 'w') as file:
        print(f"File '{file_name}' created successfully.")

# Function to write content to a file
def write_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content + '\n')
        print("Content written to the file.")

# Function to read content from a file
def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print("Content of the file:")
        print(content)

# Function to delete a file
def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print(f"File '{file_name}' does not exist.")

# Main function
def main():
    file_name = "sample.txt"
    create_file(file_name)
    write_to_file(file_name, "Hello, world!")
    read_file(file_name)
    delete_file(file_name)

if __name__ == "__main__":
    main()
        