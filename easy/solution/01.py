class ExceptionLength(Exception):
    pass


class Length(object):
    CONVERSION_FACTOR = {
        'feet': 1 / 0.3048,
        'inch': 1000 / 25.4,
        'mm': 1000,
    }

    def __init__(self, the_value):
        self.value = the_value

    def __str__(self):
        return 'Length: {0:.3f} (m)'.format(self.value)

    def convert(self, uom):
        try:
            return self.value * Length.CONVERSION_FACTOR[uom]
        except KeyError:
            raise ExceptionLength('Can not convert to: {0:s}'.format(str(uom)))

    def __add__(self, other):
        return Length(self.value + other.value)
