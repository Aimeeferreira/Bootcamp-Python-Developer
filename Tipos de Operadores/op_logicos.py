'''
AND = para ser True tudo tem que ser True
OR = para ser True apenas um tem que ser True

Seguindo da esquerda para a direita.
'''

# Exemplos simples de utilização:

print(True and True)
print(True and False)
print(False and False)
print(True and False and True)
print(False and False)

print(True or True)
print(True or False)
print(True or True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

ex = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(ex)

ex_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(ex_2)

conta_normal_com_saldo_suficiente   = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

ex_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(ex_3)