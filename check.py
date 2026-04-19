import os
import shutil
import path
import adv_path_lib

file_exists = os.path.exists("example.txt")
print(f"does example.txt exist {file_exists}")

folder_exists = os.path.exists('my_folder')
print(f"Does my folder exist {folder_exists}")