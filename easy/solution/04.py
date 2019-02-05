# ==== Задание 1:
def raise_if_not_length_four(value):
    if len(value) != 4:
        raise ValueError('Argument must be length 4, not {:d}'.format(len(value)))
    return value


# ==== Задание 2:
def raise_if_not_four_characters(value):
    if len(value) != 4:
        raise ValueError('Argument must be length 4, not {:d}'.format(len(value)))
    if type(value) is not str:
        raise TypeError('Argument must be a string, not {:s}'.format(type(value)))
    return value


# ==== Задание 3:
# ---- НЕ МЕНЯЕМ
GOOD_NETWORK = 0
BAD_NETWORK = 1


class DataBase(object):
    number_of_connections = 0

    def __init__(self, network):
        self.network = network
        DataBase.number_of_connections += 1

    def read(self):
        if self.network == BAD_NETWORK:
            raise IOError('Ooops')
        return 'Data...'

    def close(self):
        DataBase.number_of_connections -= 1


def reset():
    DataBase.number_of_connections = 0


# ---- НЕ МЕНЯЕМ


def get_data_one(network):
    db = DataBase(network)
    result = ''

    try:
        result = db.read()
    except IOError as err:
        print(err)

    db.close()

    return result


def get_data_two(network):
    db = DataBase(network)
    result = ''

    try:
        result = db.read()
    finally:
        db.close()

    return result
