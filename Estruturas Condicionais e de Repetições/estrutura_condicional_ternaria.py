# Exemplo de condição com retorno/resposta da lógica da expressão

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")