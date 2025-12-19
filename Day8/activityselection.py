start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selectedActivities = []
activities = []
for i in range(len(start)):
    activities.append((start[i], finish[i]))

print(activities)
activities.sort(key=lambda x: x[1])
print(activities)

selectedActivities.append(activities[0])

last_finished_activity = activities[0][1]

for i in range(1, len(activities)):
    current_activity = activities[i]
    if last_finished_activity <= current_activity[0]:
        selectedActivities.append(current_activity)
        last_finished_activity = current_activity[1]

print(selectedActivities)
