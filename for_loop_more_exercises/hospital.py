period_of_time = int(input())
seen_patients = 0
unseen_patients = 0
doctors_count = 7
for i in range(1, period_of_time + 1):
    num_of_patients = int(input())
    if i % 3 == 0:
        if unseen_patients > seen_patients:
            doctors_count += 1
    if num_of_patients <= doctors_count:
        seen_patients += num_of_patients
    else:
        seen_patients += doctors_count
        unseen = num_of_patients - doctors_count
        unseen_patients += unseen

print(f"Treated patients: {seen_patients}.")
print(f"Untreated patients: {unseen_patients}.")



