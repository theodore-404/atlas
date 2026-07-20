missions = []
running = True

print("=== ATLAS For Loop ===")

while running:
    missions.append(input("Mission: "))

    print("Mission added.")
    print()
    print("Current missions: ")
    for mission in missions:
        print(mission)
