"""
Напишите программу, которая итерирует слова и постоянно выполняет сортировку.

Этот генератор может быть использован следующим образом:

g = keep_sorted()
# Запускаем итерацию
g.next()
# Отправляем слово
g.send('zzz')
g.send('Hi there')
# Используем next для получения списка
print('Отсортированный список {0:s}'.format(g.next()))
g.close()
"""


def keep_sorted():
    """
    Функция, принимающая слова и сортирующая список из них (необходимо исправить код)
    """
    l = []
    while True:
        v = yield l
        if v is not None:
            l.append(v)
            l.sort()


if __name__ == '__main__':
    g = keep_sorted()
    # Запуск итерации
    g.next()
    # Отправляем слова
    print(g.send('zzz'))
    print(g.send('Hi there'))
    print('Sorted list is {0:s}'.format(g.next()))
    g.close()
