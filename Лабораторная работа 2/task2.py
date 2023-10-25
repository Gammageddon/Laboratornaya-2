salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
month = 0
money_capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

while month < months:
    spent_this_month = spend
    if month != 0:
        spend += spend * increase
        spent_this_month = spend
    money_capital += spent_this_month - salary
    month += 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))

