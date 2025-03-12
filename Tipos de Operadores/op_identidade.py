'''
Utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

Seguindo da esquerda para a direita.
'''

# Exemplos simples de utilização:

saldo = 1000
limite = 1000
print(saldo is limite)
print(saldo is not limite)

saldo = 1000
limite = 200
print(saldo is limite)
print(saldo is not limite)