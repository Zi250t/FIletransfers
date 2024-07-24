import shutil
import os

# Prompt for source file path
source_file_path = input("Enter the source file path: ").strip()

# Validate source file path
if not os.path.isfile(source_file_path):
    print(f"Error: '{source_file_path}' is not a valid file path.")
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

# Get file name from source path
file_name = os.path.basename(source_file_path)

# Construct destination path
destination_path = os.path.join(destination_dir, file_name)

# Copy file
try:
    shutil.copy2(source_file_path, destination_path)
    print("File copied successfully.")
except shutil.Error as e:
    print(f"Error copying file: {e}")
except IOError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
