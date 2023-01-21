# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше 
# предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

# def f1():
#     n = int(input('Введите количество чисел в списке: '))
#     lst = []
#     while len(lst) < n: 
#         a = randint(1, 51)
#         lst.append(a)
#     return lst   

# print('Исходный список:', f1())


n = int(input('Введите количество чисел в списке: '))
lst = []
while len(lst) < n: 
    a = randint(1, 51)
    lst.append(a)

print('исходный список:',lst)   

new_lst = []
lst = [int(i) for i in lst]
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        (new_lst.append(lst[i]))

print('элементы исходного списка, значения которых больше предыдущего элемента: ', new_lst)

    