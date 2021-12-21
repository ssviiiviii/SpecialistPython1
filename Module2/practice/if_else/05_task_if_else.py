month = int(input('введите номер месяца: '))
if month == 12 or 1 <= month <= 2:
    print('Зима')
elif 3 <= month <= 5:
    print('Весна')
elif 6 <= month <= 8:
    print('Лето')
else:
    print('Осень')
