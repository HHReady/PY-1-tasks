def select_first_items():
    x = [('A', 'x'), ('B', 'y'), ('C', 'z')]
    return [v[0] for v in x]


def rotate_left(alist):
    if len(alist):
        alist.append(alist.pop(0))


def rotate_right(alist):
    if len(alist):
        alist.insert(0, alist.pop())
