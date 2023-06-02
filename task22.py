"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

import random
n = int(input("Введите кол-во элементов в массиве -> "))
array_1 = []
for i in range(n):
    x = random.randint(0,9)
    array_1.append(x)
print(array_1)

m = int(input("Введите кол-во элементов в массиве -> "))
array_2 = []
for i in range(m):
    x = random.randint(0,9)
    array_2.append(x)
print(array_2)

plety_1 = set()
plety_2 = set()


for j in array_2:
    plety_2.add(j)


for i in array_1:
    plety_1.add(i)


#plety_1 = array_1.copy()
#plety_2 = array_2.copy()

result = plety_1.intersection(plety_2)

print(result)