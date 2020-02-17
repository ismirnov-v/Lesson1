#Задание №1:
def get_summ(one, two, delimeter = '&'):
    one = str(one).capitalize()
    two = str(two).capitalize()
    return one + delimeter + two

result = get_summ('Learn', 'python')
print(result)