import os

print("contents of current directory: ")

for item in os.listdir("."):
    print(f" - {item}")

print("\ndirectory contents: ")
for item in os.listdir("."):
    full_path = os.path.join(os.getcwd(), item)
    print(f" - {full_path}")