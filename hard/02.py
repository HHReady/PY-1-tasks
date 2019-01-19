"""
Напишите функцию, которая рандомизирует буквы в словах после первых N букв.

Функция будет называться randomWords(words, n),
где words - это список слов, а n - количество начальных букв каждого слова,
чтобы сохранить их в порядке случайного перемешивания.

Код в main вызовет вашу функцию с различными значениями n,
чтобы увидеть, сколько незашифрованного текста в каждом слове вам нужно понять.

Пример:
>> Введите текст или <enter> для выхода: Numeric is a hedge fund operating out of offices in Boston
   0: imeNucr si a deghe dfnu rntpigeao out of ifosfce in otnBso
   1: Nmuerci is a hedeg fudn oantrgiep out of ofsfcie in Bontos
   2: Nucermi is a heedg fudn opertaign out of ofiscfe in Botson
   3: Numrcei is a hedge fund operantgi out of offseic in Boston
   4: Numeicr is a hedge fund operingat out of offisec in Bostno
   5: Numeric is a hedge fund operaigtn out of offices in Boston
   6: Numeric is a hedge fund operatngi out of offices in Boston
   7: Numeric is a hedge fund operating out of offices in Boston
   8: Numeric is a hedge fund operating out of offices in Boston

Вам нужно около 4 букв, чтобы понять предложение.

СОВЕТ: random модуль полезен, он имеет функцию shuffle (последовательность),
которая возвращает случайную последовательность случайных чисел.
"""
import random


def randomWords(words, n):
    pass


def main():
    # Зацикливайтесь, пока пользователь не нажмет <enter>.
    while True:
        line = input('Введите текст или <q> для выхода: ')
        words = line.split()
        if len(words) == 0:
            # Пользователь хочет выйти
            break
        max_len = max([len(w) for w in words])
        for n in range(max_len):
            print('%4d: %s' % (n, ' '.join(randomWords(words, n))))

