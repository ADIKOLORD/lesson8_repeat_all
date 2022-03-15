"""
# 1(Множества)
# 1.Объединить 2 множества
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
all_months = months_a.update(months_b)
# all_months = set(list(months_a) + list(months_b))
print(all_months)
# 2.Добавить месяц, которого нету во множестве
# all_months.add('Dec')

# 3.Перебрать элементы множества
# Didn't understand

# 4.Вам даны 2 множества, узнать какие элементы пересекаются между ними.
x = {1, 2, 3}
y = {4, 3, 6}

print(x.intersection(y))

# 2(Словари)
# Написать скрипт который проходится по ключам и проверяет значения
# a) Если значение делиться на 3, то записываем строку “Hi”
# b) Если значение делиться на 5, то записываем строку “Bye”

# ПРИМЕР:
# Дано -> dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# Результат -> a = Bye
# b = Hi

my_dict = {}
for i in range(13):
    my_dict[i] = f'Hello {i}'
for i in my_dict:
    if i % 3 == 0:
        my_dict[i] = 'Hi'
    elif i % 5 == 0:
        my_dict[i] = 'Bye'
print(my_dict)

# 3 Напишите программу для слияния нескольких словарей в один.

my_friends = {
    "Joomart": "+996555246810",
    "Adinai": "+996555013579",
    "Ermek": "+996777013579",
    "Atai": "+996777246810",
    "Aslan": "+996999246810",
}

his_her_friends = {
    "Lyazat": "+996551123456",
    "Salavat": "+996552234567",
    "Daniyar": "+996553345678",
    "Bolot": "+996554456789",
    "Alymbek": "+996555501234",
    "Dastan": "+996556678912",
    "Maksat": "+996557789012",
    "Aibek": "+996558890123",
}

our_friends = {}
# our_friends.update(my_friends)
# our_friends.update(his_her_friends)
for my in my_friends.items():
    our_friends.update({my})
for his in his_her_friends.items():
    our_friends.update({his})
print(our_friends)


# 4
# Найдите три ключа с самыми высокими значениями в
# словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
# после чего эти ключи сохраните в какой либо переменной и удалите
# из предыдущего словаря

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
numbers = []
for i in my_dict.values():
    numbers.append(i)
one_max = max(numbers)
numbers.remove(one_max)

two_max = max(numbers)
numbers.remove(two_max)

three_max = max(numbers)
numbers.remove(three_max)

for k, v in my_dict.items():
    if v == one_max:
        one_max = k, v
        one_key = k
    elif v == two_max:
        two_max = k, v
        two_key = k
    elif v == three_max:
        three_max = k, v
        three_key = k
my_dict.pop(one_key)
my_dict.pop(two_key)
my_dict.pop(three_key)
print(one_max)
print(two_max)
print(three_max)
print(my_dict.items())




# 5
# Написать программу калькулятор оценок. Даны списки оценок с
# предметами трех студентов. В каждом списке содержиться 7
# предметов с оценками, необходимо сконвертировать в словарь и
# найти средний балл оценок данных студентов. И выбрать лучшего
# студента в группе.
# Например:
# ввод данных John = [[algebra“, 100], [„biologia“, 84], [„fizika“: 61]]
# вывод: оценки
#
# John   : {'algebra': 100, 'biologia': 84, 'fizika': 61}
# Средний балл
#
# John   : 81 балл
# Лучшим студентом является: {имя студенто у которго больше всех
# балл}
John = [['algebra', 100], ['biologia', 84], ['fizika', 61]]
Katy = [['algebra', 95], ['biologia', 90], ['fizika', 78]]
Djek = [['algebra', 89], ['biologia', 61], ['fizika', 89]]
'''Студенттерди бир жерге топтоп алабыз (list)'''
students = [John, Katy, Djek]
john_dict = {}
katy_dict = {}
djek_dict = {}
count = 1
'''Ар бир студенттин сабагын бирден карап чыгабыз'''
for student in students:
    for pred, bal in student:
        if count == 1:
            john_dict[pred] = bal
        elif count == 2:
            katy_dict[pred] = bal
        elif count == 3:
            djek_dict[pred] = bal
    count += 1
'''Алган баллдары value де болгон учун, алардын суммасын табып, сабактын санына болобуз'''
sumball_john = int(sum(john_dict.values()) / 3)
sumball_katy = int(sum(katy_dict.values()) / 3)
sumball_djek = int(sum(djek_dict.values()) / 3)


'''Алардын арасынын макс таап, кайсы стеденттин баллына барабар экенин текшеребиз'''
maxball = max(sumball_john, sumball_djek, sumball_katy)
if maxball == sumball_john:
    print(f'Лучшим студентом является: John\nПолучил(а): {sumball_john}')
elif maxball == sumball_katy:
    print(f'Лучшим студентом является: Katy\nПолучил(а): {sumball_katy}')
elif maxball == sumball_djek:
    print(f'Лучшим студентом является: Djek\nПолучил(а): {sumball_djek}')





# 6
# Создайте словарь, связав его с переменной school, и наполните
# данными, которые бы отражали количество учащихся в разных
# классах (1а, 1б, 2б, 6а, 7в и т. п.). Внесите изменения в словарь
# согласно следующему:
# а) в одном из классов изменилось количество учащихся,
# б) в школе появился новый класс,
# с) в школе был расформирован (удален) другой класс.
# Вычислите общее количество учащихся в школе.

school = {
    '1A': 24,
    '1B': 20,
    '2A': 18,
    '2B': 21,
    '3A': 19,
    '3B': 16,
    '4A': 17,
    '4B': 16,
}
# а) в одном из классов изменилось количество учащихся,
school['1A'] = 26
# б) в школе появился новый класс,
school['5A'] = 19
# с) в школе был расформирован (удален) другой класс.
school.pop('4A')

"""



