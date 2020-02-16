a = 'Прив3т т3б3 с3годня!'

print(a)

print(a.replace('3', 'е'))

print('ПриветЫ'.replace('ы', ''))
print('ПриветЫ'.lower().replace('ы', '').capitalize())

print('ПриветЫ'.lower().replace('ы', ' Python!').capitalize())

b = 'learn.python.ru'
print(b)
print(b.split('.'))

c = 'Супер предложение  с  множеством слов, которые вам придется подсчитать.'

print(c)
print(c.split())
print(len(c.split()))