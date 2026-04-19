import os,shutil,path,pathlib

def create_file(file_path, content=""):

    try:
        os.mkdir(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            file.write(content)
        print(f"{file_path} created successfully")
    except Exception as e:
        print(f"{file_path} could not be created")

##delete file
def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully")
        else:
            print(f"{file_path} could not be deleted")
    except Exception as e:
        print(f"{file_path} could not be deleted")

#rename file
def rename_file(old_path, new_name):
    try:
        if os.path.exists(old_path):
            os.makedirs(os.path.dirname(old_path), exist_ok=True)
            os.rename(old_path, new_name)
            print(f"{old_path} -> {new_name} renamed successfully")
        else:
            print(f"{old_path} could not be renamed")
    except Exception as e:
        print(f"Error renaming file: {e}")
        return False

def main():
    print("current working directory", os.getcwd())

    test_file = "test_file.txt"
    print(f"Attempting to create file {test_file}")

    if create_file(test_file, "this is a test sample"):
        if rename_file(test_file, "rename_file.txt"):
            delete_file("rename_file.txt")

    sub_file = "sub_folder/test_file.txt"
    print(f"\nAttempting to create file {sub_file}")

    if create_file(sub_file, "this is a file in subdirectory"):
        delete_file(sub_file)
        try:
            os.rmdir("test_folder")
        except:
            pass







if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()




