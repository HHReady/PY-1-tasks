import csv


def read_csv_hard(file_name='data.csv'):
    raw_result = []

    with open(file_name) as f:
        reader = csv.reader(f)

        for row in reader:
            raw_result.append(row)

    keys = raw_result[0]
    result = []

    for row in raw_result[1:]:
        result.append({keys[i]: val for i, val in enumerate(row)})

    return result


def read_csv_easy(file_name='data.csv'):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
