def welcome():
    print("Acces Granted.")
    print("Welcome, Commander.")

def denied():
    print("Access Denied.")
    print("Unknown User.")

print("=== ATLAS Functions ===")
name = input("Enter your name: ")
if name == "Wynn":
    welcome()
else:
    denied()
