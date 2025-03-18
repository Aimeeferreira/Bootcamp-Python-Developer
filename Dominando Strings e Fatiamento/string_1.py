#Modifying strings with Upper, Lower, Title, Strip, LStrip, RStrip, Center and Join commands.

nome = "AiMee"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Hello World!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))
