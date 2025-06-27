import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')
files = os.listdir()

for file in files:
    # Skip directories in the list
    if os.path.isdir(file):
        continue

    if file == 'script.py':
        continue

    # Safely split filename and get extension
    if '.' in file:
        extension = file.split('.')[-1]  # Use -1 for file extension
    else:
        continue  # skip files without extension

    # Create folder if it doesn't exist
    if not os.path.exists(extension):
        os.mkdir(extension)

    source_path = os.path.join(os.getcwd(), file)  # <- FIX: add parentheses to os.getcwd()
    destination_path = os.path.join(os.getcwd(), extension, file)

    shutil.move(source_path, destination_path)
    print(f"Moved {file} to {extension}/")