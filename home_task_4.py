result = []


def problemsindict(*args): #Це трішки епічно
    dictionary = {}
    for i in range(1, len(args), 2):
        if not type(args[i]) == list and not type(args[i - 1]) == list:
            dictionary.update([(args[i - 1], args[i])])
        else:
            if type(args[i]) == list:
                element1 = str(args[i])
            else:
                element1 = args[i]
            if type(args[i - 1]) == list:
                element2 = str(args[i - 1])
            else:
                element2 = args[i - 1]
            dictionary.update([(element2, element1)])
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


data = problemsindict(10, 2, 2, 5, "123", 4, 18, 0, [], 15, 8, 4)

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as exc:
        result.append(exc)

print(result)
