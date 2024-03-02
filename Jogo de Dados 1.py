#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Programa do dia 01/03/2024

import random

class Dados:

    def __init__(self, qtd_de_dado, numero_de_vezes):
        self.qtd_de_dado = qtd_de_dado
        self.numero_de_vezes = numero_de_vezes
        self.lado_dado = []
        self.soma_dado = []
        self.total = self.qtd_de_dado * 6 + 1
        self.lista_dado()
        self.joga_dado()
        self.imprimir()

    def lista_dado(self):
        for tamanho in range(self.qtd_de_dado, self.total):
            self.lado_dado.insert(tamanho, tamanho)
            self.soma_dado.insert(tamanho, 0)

    def joga_dado(self):
        for i in range(self.numero_de_vezes):
            dado = 0
            for j in range(self.qtd_de_dado):
                dado = dado + random.randint(1, 6)
            for j in range(self.total - self.qtd_de_dado):
                if dado == self.lado_dado[j]:
                    self.soma_dado[j] = self.soma_dado[j] + 1
                    break

    def imprimir(self):
        # Imprimir o resultado da soma dos lados e quantidade de vezes que se repetem.
        for i in range(self.total - self.qtd_de_dado):
            print('(' + str(self.lado_dado[i]) + '):', end = ' ')
            print(self.soma_dado[i])

if __name__ == '__main__':
    while True:
        try:
            qtd_de_dado = int(input("Informe a quantidade de dados: "))
            numero_de_vezes = int(input("Informe a quantidade de número de vezes que os dados serão jogados: "))
            Dados(qtd_de_dado, numero_de_vezes)
            break
        except:
            print('Número Inválido. Digite novamente.')