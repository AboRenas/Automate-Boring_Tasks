import os
import shutil

if os.path.exists("destination_file.txt"):
    os.remove("destination_file.txt")
    print("File removed")

if os.path.exists("empty_folder"):
    os.rmdir("empty_folder")
    print("Folder removed successfully")

if os.path.exists("parent_folder"):
    shutil.rmtree("parent_folder")
    print("Folder removed successfully")