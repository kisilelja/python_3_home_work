# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

a = int(input("Введите размер списка: "))
list = list(range(1, a + 1))
print(list)
b=int(input('Введите искомый элемент Х: '))
number = 0
for i in range(len(list)):
    if (b-list[i])<b-number and b-list[i]>0:
        number=i
print(list[number])