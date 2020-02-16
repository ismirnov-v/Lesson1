price = 15000
discount = 5

price_with_discount = price * (1-discount/100)

print(f'Цена без скидки: {price} \nЦена со скидкой: {price_with_discount}')

print('Подсчеты далее выполены с использованием функции.')

def discounted(price, discount):
    price_with_discount = price * (1 - discount/100)
    print(price_with_discount)

discounted(price, 10)