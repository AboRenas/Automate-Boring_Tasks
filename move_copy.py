import os
import shutil
import adv_path_lib as path

with open('source_file.txt', 'w') as file:
    file.write('this is a source file.')


shutil.copy('source_file.txt', 'destination_file.txt')

print("file copy successful")

shutil.move("source_file.txt", "my_folder/moved_file.txt")
print("file moved successful")