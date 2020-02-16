# Практика: Числа
# 
v = int(input('Введите число от 1 до 10: '))
print(v)

# На дессять больше:
print(v + 10)


#
# Практика: Строки
name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

#
#  Практика Приведение типов
# 
# Если оставить 2.5 в кавычках то при компиляции получаю ошибку)
#  Traceback (most recent call last):
#   File "c:/Projects/Lesson1/Lesson1-homework/data_type.py", line 26, in <module>
#    ''')
# ValueError: invalid literal for int() with base 10: '2.5'


print (
    f'''
    float('1'):\t {float('1')},
    int(2.5):\t {int(2.5)},
    bool(1):\t {bool(1)},
    bool(''):\t {bool('')},
    bool(0):\t {bool(0)},
    ''')