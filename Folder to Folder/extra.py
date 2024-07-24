import shutil
import os

# Prompt for source folder path
source_folder_path = input("Enter the source folder path: ").strip()

# Validate source folder path
if not os.path.isdir(source_folder_path):
    print(f"Error: '{source_folder_path}' is not a valid directory.")
    exit(1)

# Prompt for destination directory
destination_dir = input("Enter the destination directory: ").strip()

# Validate destination directory
if not os.path.exists(destination_dir):
    try:
        os.makedirs(destination_dir)
    except OSError as e:
        print(f"Error creating destination directory '{destination_dir}': {e}")
        exit(1)

if not os.path.isdir(destination_dir):
    print(f"Error: '{destination_dir}' is not a valid directory.")
    exit(1)

# Get list of all files in source folder
files = os.listdir(source_folder_path)

# Copy each file to the destination directory
for file_name in files:
    source_file_path = os.path.join(source_folder_path, file_name)
    destination_path = os.path.join(destination_dir, file_name)
    
    try:
        shutil.copy2(source_file_path, destination_path)
        print(f"File '{file_name}' copied successfully.")
    except shutil.Error as e:
        print(f"Error copying file '{file_name}': {e}")
    except IOError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

print("All files copied.")
