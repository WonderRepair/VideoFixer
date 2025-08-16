import os
import time

# Ask user for folder path
folder = input("Enter the folder path: ")

# Check if folder exists
if not os.path.isdir(folder):
    print("Folder not found!")
    exit()

# Get all files in the folder
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

num_files = len(files)
if num_files == 0:
    print("No files found in the folder.")
    exit()

print(f"\nFound {num_files} files. Starting to 'fix' them...\n")


total_time = 20 * 60


delay_per_file = total_time / num_files

# Loop through each file once
for file_name in files:
    print(f"Fixing file: {file_name}")
    time.sleep(delay_per_file)

print("\nAll files 'fixed'! ✅")
