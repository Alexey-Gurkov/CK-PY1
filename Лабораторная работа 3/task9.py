salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    need_money_1month = spend - salary
    need_money += need_money_1month
    spend *= (1 + 0.03)

print(round(need_money))
