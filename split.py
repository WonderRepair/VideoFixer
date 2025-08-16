import os

# Ask user for input folder
INPUT_FOLDER = input("Enter the path to the folder containing files to split: ").strip()

# Output folder (created automatically)
OUTPUT_FOLDER = "split_files"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

CHUNK_SIZE = 80 * 1024 * 1024  # 80 MB

for filename in os.listdir(INPUT_FOLDER):
    filepath = os.path.join(INPUT_FOLDER, filename)
    if not os.path.isfile(filepath):
        continue

    with open(filepath, "rb") as f:
        chunk_num = 1
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            chunk_filename = f"{filename}.part{chunk_num:03d}"
            chunk_path = os.path.join(OUTPUT_FOLDER, chunk_filename)
            with open(chunk_path, "wb") as chunk_file:
                chunk_file.write(chunk)
            print(f"Created {chunk_path}")
            chunk_num += 1

print(f"All files in '{INPUT_FOLDER}' split successfully into '{OUTPUT_FOLDER}'!")
