stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'recomend': ['Samsung S10', 'iPhone Xs'] },
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 30000.5}
]

print(stock[1])
print(stock[2])
print(stock[0])

print(stock[0]["recomend"])

print(type(stock[2]))

print(stock[0]["price"])

stock[0]["price"] += 213450

print(stock[0]["price"])