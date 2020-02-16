price = 15000
discount = 5

price_with_discount = price * (1-discount/100)

print(f'Цена без скидки: {price} \nЦена со скидкой: {price_with_discount}')

print('Подсчеты далее выполены с использованием функции.')

def discounted(price, discount):
    """ Функция для подсчета цены со скидкой.
    """
    price = abs(float(price))
    discount = abs(float(discount))

    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price * (1 - discount/100)
    print(price_with_discount)

discounted(price, 10)

discounted(-5600, 27)