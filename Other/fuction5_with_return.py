price = 15000
discount = 5

price_with_discount = price * (1-discount/100)

print(f'Цена без скидки: {price} \nЦена со скидкой: {price_with_discount}')

print('Подсчеты далее выполены с использованием функции.')

def discounted(price, discount, max_discount = 50):
    """ Функция для подсчета цены со скидкой.
    """
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))

    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 99%')

    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price * (1 - discount/100)
    
    return price_with_discount

p = discounted(price, 10)

p2 = discounted(-5600, 27)

print(p, p2)
product = {
    "name": "iPhone Xs",
    "stock": 24,
    "price": 65432.1,
    "discount": 79
}

product["with_discount"] = discounted(product['price'], product['discount'], 80)
print(product)

p3 = discounted(price, 100, 100)

print(p3)