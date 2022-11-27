a = ['hello','123','world','1']
i = 0
while i < len(a):
    if len(a[i]) > 3:
        a.pop(i)
    i = i + 1
print(a)