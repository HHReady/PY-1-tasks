def keep_sorted():
    result_list = []
    while True:
        v = yield result_list
        if v is not None:
            result_list.append(v)
            result_list.sort()


if __name__ == '__main__':
    g = keep_sorted()
    # Запуск итерации
    next(g)
    # Отправляем слова
    print(g.send('zzz'))
    print(g.send('Hi there'))
    print('Sorted list is {0:s}'.format(str(next(g))))
    g.close()
