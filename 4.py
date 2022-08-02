a = [1, 5, 6, 7, 8, 9 ,10]
with open('one.txt', 'w') as f:
    for i in a:
        f.write(str(i) + '\n')

