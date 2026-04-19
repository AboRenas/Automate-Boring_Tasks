import os

file_path = 'example.txt'
if os.path.exists(file_path):
    file_info = os.stat(file_path)
    print(f"file: {file_path}")
    print(f"Size: {file_info.st_size} bytes")
    print(f"Last modified: {file_info.st_mtime}")
    print(f"Is file: {os.path.isfile(file_path)}")
    print(f"Is directory: {os.path.isdir(file_path)}")