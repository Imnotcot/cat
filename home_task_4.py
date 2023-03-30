result = []


def problemsindict(*args): #Це трішки епічно
    dictionary = {}
    for i in range(len(args)):
        if not type(args[i][0]) == list:
            dictionary.update([(args[i][0], args[i][1])])
        else:
            dictionary.update([(str(args[i][0]), args[i][1])])
    return dictionary


def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a/b
    except Exception as exc:
        return exc


data = problemsindict([10, 2], [2, 5], ["123", 4], [18, 0], [[], 15], [8, 4])

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as exc:
        result.append(exc)

print(result)
