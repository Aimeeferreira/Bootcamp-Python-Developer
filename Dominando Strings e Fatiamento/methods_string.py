#Modifying strings with Upper, Lower, Title, Strip, LStrip, RStrip, Center and Join methods.

name = "AiMee"

print(name.upper())
print(name.lower())
print(name.title())

text = "  Hello World!    "

print(text + ".")
print(text.strip() + ".")
print(text.rstrip() + ".")
print(text.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))
