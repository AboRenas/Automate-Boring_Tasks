print("Reading line by line")

with open("example1.txt", 'r') as f:
    for line_number, line in enumerate(f,1):
        print(f"{line_number}: {line.strip()}")

