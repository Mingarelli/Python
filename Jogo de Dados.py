import random

qtd_de_dado = int(input("Informe a quantidade de dados: "))
numero = int(input("Informe a quantidade de número de vezes que os dados serão jogados: "))
lado_dado = []
soma_dado = []

total = qtd_de_dado * 6 + 1

for i in range(qtd_de_dado, total):
    lado_dado.insert(i , i)
    soma_dado.insert(i, 0)

for i in range(numero):
    dado = 0
    for j in range(qtd_de_dado):
        dado = dado + random.randint(1,6)
    for j in range(total - qtd_de_dado):
        if dado == lado_dado[j]:
            soma_dado[j] = soma_dado[j] + 1
            break
        else:
            pass

for i in range(total - qtd_de_dado):
    print("(" + str(lado_dado[i]) + "): ", end ='')
    print(soma_dado[i])

