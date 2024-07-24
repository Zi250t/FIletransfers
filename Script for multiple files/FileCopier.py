import shutil
import os

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

# List to store source file paths
source_files = []

# Prompt user to enter each source file path
while True:
    source_file_path = input("Enter source file path (or 'q' to quit): ").strip()
    
    if source_file_path.lower() == 'q':
        break
    
    if os.path.isfile(source_file_path):
        source_files.append(source_file_path)
    else:
        print(f"Invalid file path: {source_file_path}")

# Copy each file to the destination directory
for source_file_path in source_files:
    file_name = os.path.basename(source_file_path)
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