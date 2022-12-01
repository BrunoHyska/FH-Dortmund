l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (2, 2, 1)]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i][-1] > l[j][-1]:
            l[i], l[j] = l[j], l[i]

print(l)
