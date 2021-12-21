quantity = 1
price = float(input('Введите стоимость товара: '))
while quantity <= 20:
    print (quantity, round(quantity * price, 2), 'Rub')
    quantity += 1
