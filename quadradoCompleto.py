import os

x = int(input("Digite o valor da largura: "))
y = int(input("Digite o valor da altura: "))
char = "#"

def ret(char, x, y):
    cheia = char * x
    if x > 2:
        vazia = char + ("#" * (x - 2)) + char
    else:
        vazia = cheia
    if y >= 1:
        print(cheia)
    for i in range(y - 2):
        print(vazia)
    if y >= 2:
        print(cheia)

ret(char, x, y)

os.system("pause")
