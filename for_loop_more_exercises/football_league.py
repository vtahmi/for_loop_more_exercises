stadium_capacity = int(input())
total_fans = int(input())
A = 0
B = 0
V = 0
G = 0
for num in range(total_fans):
    sector = input()
    if sector == "A":
        A += 1
    elif sector == "B":
        B += 1
    elif sector == "V":
        V += 1
    elif sector == "G":
        G += 1

percent_fans_A = A / total_fans * 100
percent_fans_B = B / total_fans * 100
percent_fans_V = V / total_fans * 100
percent_fans_G = G / total_fans * 100
percent_total_fans = total_fans / stadium_capacity * 100
print(f"{percent_fans_A:.2f}%")
print(f"{percent_fans_B:.2f}%")
print(f"{percent_fans_V:.2f}%")
print(f"{percent_fans_G:.2f}%")
print(f"{percent_total_fans:.2f}%")
