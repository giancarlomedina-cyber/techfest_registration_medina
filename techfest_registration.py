print("Welcome to SMIT TechFest")
print("Event organized by Gian Carlo of APPDAET BTCS2")

num_participants = int(input("How many participants will register?: "))

if num_participants <= 0:
    print("Invalid number of participants")
else:
    participants = num_participants

participants = []  # List to store participants' data

for i in range(num_participants):
    print(f"\nEntering details for participant {i + 1}:")
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")

    # Store each record as a dictionary and append it to the list
    participant = {
        "name": name,
        "track": track
    }
    participants.append(participant)