import re


def digits(m):
    assert (m is not None)
    return int(m.group(1)) / 2


def letters(m):
    assert (m is not None)
    return m.group(1).lower()


RE_OPTIONS = (
    (re.compile(r'^(\d+)$'), digits),
    (re.compile(r'^(\D+)$'), letters),
)


def match_lines(input_lines):
    result = []

    for line in input_lines:
        for pattern, function in RE_OPTIONS:
            m = pattern.match(line)

            if m is not None:
                result.append(function(m))
                break
        else:
            result.append(None)

    return result


def main():
    text = """288
ABCDEFGH
1A2B3C4D

Hello world
42"""
    result = match_lines(text.split('\n'))
    print(result)
