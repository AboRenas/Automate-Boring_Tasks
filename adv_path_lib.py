import os,shutil
from pathlib import Path


from file_info import file_info
from read import content

current_dir = Path('.')
file_path = Path('example.text')

print(f"File exists: {file_path.exists()}")

if file_path.exists():
    print(f"file name: {file_path.name}")
    print(f"Size: {file_path.stem} bytes")
    print(f"File suffix : {file_path.suffix}")
    print(f"File parent: {file_path.parent}")
    print(f"Absolute path: {file_path.absolute()}")

new_dir = Path('new_directory')
new_dir.mkdir(exist_ok=True)
new_file = new_dir / 'new_file.text'
new_file.write_text('Hello World! which means is working and functional')

content = new_file.read_text()
print(f"Content of the new file:{content}")
