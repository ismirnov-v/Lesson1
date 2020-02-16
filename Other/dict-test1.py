product = {
    "name": "iPhone Xs",
    "stock": 24,
    "price": 65432.1
}

print(len(product))
print(product)

product["memory"] = 64
print(product)


product["name"] = 'iPhone Xs Plus'
print(f'В словаре изменили значение ключа "name".\n {product}')

print(product.get('name'))

print(product.get('discount', 0))

del product["stock"]

print(product)


phones = ["iPhone Xs", "Samsung 10s", "Xiaomi Mi8"]

product["recomend"] = phones

print(product)


print(product["recomend"][1])
product["recomend"].append("iPhone 6s")
print(product)