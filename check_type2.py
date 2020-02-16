a = 2.0
b = '22'
c = "sq"
d = True
e = None
f = []
g = {}


#print('------------')
#print(f'{type(a)}, {type(b)}, {type(c)}, {type(d)}, {type(e)}, {type(f)}, {type(g)}')
#lists = [a, b, c, d, e, f, g]
#print('------------')



phones = ["iPhone Xs", "Samsung 10s", "Xiaomi Mi8"]

print(phones)
phones_count = len(phones)

print(f'Тип: {type(phones)}; \nКол-во элементов: {phones_count};')

phones.append("iPhone 6")
print(phones)


print(f'Количество "iPhone Xs" в списке: {phones.count("iPhone Xs")}')
print(phones.count("new1"))



print(f'Элемент №1: {phones[1]}')
print(f'Элемент №0: {phones[0]}')
#print(f'Элемент №8: {phones[8]}')


print(phones[-1])

print(f'Индекc "Samsung 10s" в списке равен: {phones.index("Samsung 10s")}')


phones.sort()

print(phones)

print(f'Элемент "Samsung 10s" в списке? Ответ: {"Samsung 10s" in phones}')


del phones[0]

print(phones)

phones.remove('iPhone 6')

print(phones)
