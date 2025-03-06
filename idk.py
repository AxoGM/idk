import os

# Step 1: Define directory and file names
dir_name = "student_data"
file_name = "students.txt"
file_path = os.path.join(dir_name, file_name)

try:
    # Step 2: Check if directory exists, create if not
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # Step 3: Create and write to the file
    with open(file_path, "w") as file:
        file.write("Khaleef\nKhayla\nKhiyar\n")

    # Step 4: Read and display file content
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:\n" + content)

except OSError as e:
    print(f"An error occurred: {e}")
