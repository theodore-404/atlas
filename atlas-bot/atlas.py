running = True
missions = []

def hello():
    print("Hello, Wynn.")

def showMission():
    if missions:
        for number, mission in enumerate(missions, start=1):
            print(f"{number}. {mission}")
    else:
        print("No mission.")

def mission():
    print("Mission Menu")
    print()
    showMission()
    while True:
        mission = input("Mission: ")
        if mission == "delete":
            while True:
                number = int(input("Mission Number: "))
                missions.pop(number - 1)
                print("Mission deleted.")
                showMission()

                if number == "exit":
                    break
        elif mission == "exit":
            break
        
        missions.append(mission)
        print("Mission added.")
        print()
        showMission()


def finance():
    print("Finance Menu")

print("=== ATLAS BOT ===")
while running:
    command = input("Command: ")
    if command == "hello":
        hello()
    elif command == "missions":
        mission()
    elif command == "finance":
        finance()
    elif command == "exit":
        running = False
    else:
        print("Unknown Command.")