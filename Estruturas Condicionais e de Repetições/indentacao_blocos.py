# O código só irá funcionar se estiver na indentação correta. Exemplo: 

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado com sucesso!")
        print("Retire o seu dinheiro na boca do caixa eletrônico")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia.")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)