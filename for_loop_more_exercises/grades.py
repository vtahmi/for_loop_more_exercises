students = int(input())
between_2_00_2_99 = 0
between_3_00_3_99 = 0
between_4_00_4_99 = 0
over_5 = 0
average_grade = 0
for num in range(1, students + 1):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        between_2_00_2_99 += 1
        average_grade += grade
    elif 3.00 <= grade <= 3.99:
        between_3_00_3_99 += 1
        average_grade += grade
    elif 4.00 <= grade <= 4.99:
        between_4_00_4_99 += 1
        average_grade += grade
    elif grade >= 5:
        over_5 += 1
        average_grade += grade
total_grades = between_2_00_2_99 + between_3_00_3_99 + between_4_00_4_99 + over_5
total_average = average_grade / total_grades
percent_over_5 = over_5 / total_grades * 100
percent_between_4_00_4_99 = between_4_00_4_99 / total_grades * 100
percent_between_3_00_3_99 = between_3_00_3_99 / total_grades * 100
percent_between_2_00_2_99 = between_2_00_2_99 / total_grades * 100


print(f"Top students: {percent_over_5:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_4_00_4_99:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_3_00_3_99:.2f}%")
print(f"Fail: {percent_between_2_00_2_99:.2f}%")
print(f"Average: {total_average:.2f}")


