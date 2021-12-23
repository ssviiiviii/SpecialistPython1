item = {
    "name": "Кроссовки", 
    "price": "7540.5", 
    "currency": "rub", 
    "count": "10"
    
}
dollar_rate = 74.12
if item.get("name") == "Кроссовки":
    summ = float((item.get("price"))) * dollar_rate
    print(f'{summ} $')
