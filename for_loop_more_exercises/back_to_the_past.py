inherited_money = float(input())
year_to_live = int(input())
total = 0
current_years = 18
for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        total += 12000
    else:
        if i == 1801:
            current_years += 1
        else:
            current_years += 2
        extra_cash = 50 * current_years + 12000
        total += extra_cash
if inherited_money >= total:
    extra = inherited_money - total
    print(f"Yes! He will live a carefree life and will have {extra:.2f} dollars left.")
else:
    short = total - inherited_money
    print(f"He will need {short:.2f} dollars to survive.")
