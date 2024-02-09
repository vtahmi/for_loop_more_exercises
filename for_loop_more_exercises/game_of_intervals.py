num_moves = int(input())
total_points = 0
from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0
invalid_number = 0
for _ in range(num_moves):
    points = int(input())
    if 0 <= points <= 9:
        total_points += points * 0.2
        from_0_9 += 1
    elif 10 <= points <= 19:
        total_points += points * 0.3
        from_10_19 += 1
    elif 20 <= points <= 29:
        total_points += points * 0.4
        from_20_29 += 1
    elif 30 <= points <= 39:
        total_points += 50
        from_30_39 += 1
    elif 40 <= points <= 50:
        total_points += 100
        from_40_50 += 1
    else:
        invalid_number += 1
        total_points /= 2
from_0_9_percent = from_0_9 / num_moves * 100
from_10_19_percent = from_10_19 / num_moves * 100
from_20_29_percent = from_20_29 / num_moves * 100
from_30_39_percent = from_30_39 / num_moves * 100
from_40_50_percent = from_40_50 / num_moves * 100
invalid_number_percent = invalid_number / num_moves * 100
print(f"{total_points:.2f}")
print(f"From 0 to 9: {from_0_9_percent:.2f}%")
print(f"From 10 to 19: {from_10_19_percent:.2f}%")
print(f"From 20 to 29: {from_20_29_percent:.2f}%")
print(f"From 30 to 39: {from_30_39_percent:.2f}%")
print(f"From 40 to 50: {from_40_50_percent:.2f}%")
print(f"Invalid numbers: {invalid_number_percent:.2f}%")

