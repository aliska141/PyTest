
a = list()
for i in range(len(a)+1):
    if i not in a:
        a.append(i)


a[0] = 5
print(a)
