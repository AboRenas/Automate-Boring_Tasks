def main():
    with open("example2.txt", "w") as file:
        file.write("Hello World\n")
        file.write("This is a text file created during practice.\n")

with open("example2.txt", "a") as file:
    file.write("This is an appended line.\n")

print('Reading the text file: *')
with open("example2.txt", "r") as file:
    content = file.read()
    print(content)

print("Reading the file line by line : *")
with open("example2.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")

if __name__ == '__main__':
    main()
    try:
        with open('nonexistent.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File was not found")
    except IOError:
        print("I/O error occurred")