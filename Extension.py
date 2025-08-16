import os
import time
import sys

# Ask user for folder path
folder_path = input("Enter the folder path: ").strip()

if not os.path.isdir(folder_path):
    print("Invalid folder path!")
    exit()

print("Repairing in process...")

# Size threshold in bytes (1 MB)
size_threshold = 1 * 1024 * 1024

# Get all files
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
total_files = len(files)

# Function to display progress bar
def progress_bar(current, total, bar_length=40):
    fraction = current / total
    filled_length = int(bar_length * fraction)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r[{bar}] {current}/{total}')
    sys.stdout.flush()

# Process files
for i, filename in enumerate(files, 1):
    full_path = os.path.join(folder_path, filename)
    
    # Get file size
    size = os.path.getsize(full_path)
    
    # Decide new extension
    new_ext = ".jpg" if size < size_threshold else ".mp4"
    
    # Rename the file
    base_name = os.path.splitext(filename)[0]
    new_full_path = os.path.join(folder_path, base_name + new_ext)
    os.rename(full_path, new_full_path)
    
    # Update progress bar
    progress_bar(i, total_files)
    time.sleep(0.05)  # optional small delay for better visualization

print("\nRepair completed!")
