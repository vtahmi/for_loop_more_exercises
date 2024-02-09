months = int(input())
electricity = 0
water = 20 * months
internet = 15 * months
for num in range(months):
    electricity_bill = float(input())
    electricity += electricity_bill
other = (electricity + water + internet) * 1.20
average = (electricity + water + internet + other) / months
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")

