from random import randint


def list_generator():
    res = []
    for i in range(randint(1, 50)):
        res.append(randint(-100, 100))

    return res


print(list_generator())
