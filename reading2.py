with open("example.txt","r") as file:
    partial_content = file.read(15)
    print(f"first 15 characters: {partial_content}")

    file.seek(0)
    first_line = file.readline()
    print(f"second 15 characters: {first_line.strip()}")

    remaining_line = file.readline()
    print("remaining lines: ")
    for line in remaining_line:
        print(f" - {line.strip()}")


