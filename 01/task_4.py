def counting_deposit_money(amount, years, percent):
    for i in range(years):
        amount = (amount * percent / 100) + amount
    return amount


print(counting_deposit_money(1000, 3, 15))