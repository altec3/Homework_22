CSV = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read_data(csv=CSV)
    data = _sort_data(data)
    return _filter_data(data)


def _read_data(csv):
    return [x.split(';') for x in csv.split('\n')]


def _sort_data(data):
    return sorted(data, key=lambda x: int(x[1]))


def _filter_data(data):
    return [x for x in data if int(x[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
