print("=== ATLAS Loops ===")
print("ATLAS ONLINE")

running = True

while running:
    command = input("Command: ")
    if command == "hello":
        print("Hello, Wynn.")
    elif command == "mission":
        print("There is no mission.")
    elif command == "finance":
        print("Safe.")
    elif command == "exit":
        running = False
    else:
        print("Undefined.")