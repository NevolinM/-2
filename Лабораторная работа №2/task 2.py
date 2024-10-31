salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
month = 0
while True:
    if month == months:
        break
    money_capital += salary - spend
    month += 1
    spend += spend * increase
money_capital = int(abs(money_capital))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)


!!!Исправленный вариант ниже !!!
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(0, months):
    money_capital += salary - spend
    spend += spend * increase
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(abs(money_capital)))
