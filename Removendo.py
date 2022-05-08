import os

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [1, 2, 1, 3, 4, 11, 3, 6, 4, 7, 6, 7, 8, 10 ,9, 11]

lista = remove_repetidos(lista)
print (lista)

os.system("pause")