print("Генераторные сборки")


first = ['Strings', 'Student', 'Computers', 'Win95']
second = ['Строка', 'Урбан', 'Компьютер', 'OS/2.']

"""
В переменную first_result запишите генераторную сборку, которая высчитывает разницу
длин строк из списков first и second, если их длины не равны. Для перебора строк
попарно из двух списков используйте функцию zip.

В переменную second_result запишите генераторную сборку, которая содержит результаты
сравнения длин строк в одинаковых позициях из списков first и second. Составьте эту
сборку НЕ используя функцию zip. Используйте функции range и len.
"""


first_result = (len(s1) - len(s2) for s1, s2 in zip(first, second) if len(s1) != len(s2))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результата
print(list(first_result))
print(list(second_result))