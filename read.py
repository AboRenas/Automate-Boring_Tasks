with open('example.txt','r') as file:
    content = file.read()
    print("File Contents: ")
    print(content)

print("\nReading line by line: " )
with open('example.txt','r') as file:
    for line in file:
        print(line.strip())