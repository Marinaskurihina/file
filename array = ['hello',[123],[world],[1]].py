array = ['hello','123','world','1']
i = 0
while i < len(array):
    if len(array[i]) > 3:
        array.pop(i)
    i = i + 1