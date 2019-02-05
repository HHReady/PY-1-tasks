import random


def random_words(words, n):
    ret_val = []
    for word in words:
        prefix = word[:n]
        suffix = list(word[n:])
        random.shuffle(suffix)
        ret_val.append(prefix + ''.join(suffix))
    return ret_val


def main():
    while True:
        line = input('Words please, <cr> to exit: ')
        words = line.split()

        if len(words) == 0:
            # User wants to quit
            break

        max_len = max([len(w) for w in words])

        for n in range(max_len):
            print(
                '%4d: %s' % (n, ' '.join(random_words(words, n)))
            )
