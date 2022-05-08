import os

x=int(input("Digite um numero inteiro "))
y=int(input("Digite um numero inteiro "))
z=int(input("Digite um numero inteiro "))

if (x<y):
    if (y<z):
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")
os.system("pause")

