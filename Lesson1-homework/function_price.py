#Фунцкии, задание №2:

def format_price(price):
    price = abs(int(price))
    return f'Цена: {price} руб.'

price = 56.24
price_with_format = format_price(price)
print(price_with_format)