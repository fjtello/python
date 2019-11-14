listaColores = ["rojo", "naranja", "amarillo", "verde", "azul", "añil", "violeta"]
listaRainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

lista_traducido = list(map(lambda x: listaRainbow[listaColores.index(x)], listaColores))
lista_translated = list(map(lambda x: listaColores[listaRainbow.index(x)], listaRainbow))

print(lista_traducido)
print(lista_translated)