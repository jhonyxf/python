lista = []
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'igual', x, '*', n/x)
            break
    else:
        lista.append(n)
        print(n, 'eh numero primo')


print(len(lista))
print(lista)
