import os

os.makedirs('my_folder', exist_ok=True)
print("Directory created successfully")

os.makedirs('parent_folder/child_folder/grandchild_folder', exist_ok=True)
print("nested directories created successfully")