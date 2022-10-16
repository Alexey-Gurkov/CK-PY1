money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0


while money_capital > spend:
    spend *= (1 + increase)
    loss = salary - spend       #убыток
    money_capital += loss
    month += 1

print(month)
