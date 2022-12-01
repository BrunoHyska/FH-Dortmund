def convert(string):
    list1 = list(string.split())
    return list1


L = ['bruno', 'brun', 'bru', 'br', 'b']
result = map(convert, L)
print(list(result))
