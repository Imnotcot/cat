a = [[1], 2, 3, 4]
b = {}
for i in range(1, len(a), 2):
    if not type(a[i]) == list and not type(a[i-1]) == list:
        b.update([(a[i - 1], a[i])])
    else:
        if type(a[i]) == list:
            element1 = str(a[i])
        else:
            element1 = a[i]
        if type(a[i-1]) == list:
            element2 = str(a[i-1])
        else:
            element2 = a[i-1]
        b.update([(element2, element1)])
print(b)