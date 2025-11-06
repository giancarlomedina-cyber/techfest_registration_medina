print("Welcome to SMIT TechFest")
print("Event organized by Gian Carlo of APPDAET BTCS2")

num_participants = int(input("How many participants will register?: "))

if num_participants <= 0:
    print("Invalid number of participants")
else:
    participants = num_participants

participants = []

for i in range(num_participants):
    print(f"\nEntering details for participant {i + 1}:")
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")


    participant = {
        "name": name,
        "track": track
    }
    participants.append(participant)

print("\nRegistered Participants:")
for i in range(len(participants)):
    participant = participants[i]
    print(f"{i + 1}. {participant['name']} - {participant['track']}")

unique_tracks = set(participant['track'] for participant in participants)
print("\nTracks offered in this event:", ", ".join(unique_tracks))
if len(unique_tracks) < 2:
        print("Not enough variety in tracks.")

names_seen = set()
duplicate_found = False

for participant in participants:
    if participant['name'] in names_seen:
        print(f"Duplicate name found: {participant['name']}")
        duplicate_found = True
        break
    names_seen.add(participant['name'])

if not duplicate_found:
    print("No duplicate names.")

track_summary = {}

for participant in participants:
    track = participant['track']
    if track in track_summary:
        track_summary[track] += 1
    else:
        track_summary[track] = 1


print("\nParticipants per track:")
for track, count in track_summary.items():
    print(f"{track}: {count}")

