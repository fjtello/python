cifras = 5


def ordenar(n, s):
    m = list(str(n))
    m.sort(reverse=(1==s))
    previo = int("".join(m))

    final = previo
    if previo < numero_inicial:
        if s == 1:
            final = int((str(previo) + "0" * cifras)[:cifras])

    return final


def evolucion(n):
    numero_az = ordenar(n, 0)
    numero_za = ordenar(n, 1)
    numero_dif = numero_za - numero_az

    if serie_actual.__contains__(numero_dif):
        if not numeros_de_kaprekar.__contains__(numero_dif):
            numeros_de_kaprekar.append(numero_dif)
        return 0

    serie_actual.append(numero_dif)

    procesados.append(numero_dif)
    procesados.sort()
    return evolucion(numero_dif)

serie_actual = []
numero_inicial = int("1" + ("0" * (cifras - 1)))
numero_final = int("1" + "0" * cifras) - 1

numeros_de_kaprekar = []

print(" ==> Desde [ ", numero_inicial, " ] hasta [ ", numero_final, " ]")

tablero = [[0,[0,0],0]]
procesados = []

for numero in range (numero_inicial, numero_final + 1):
    fin_de_ciclo = False
    numero_en_estudio = numero

    while fin_de_ciclo == False:

        serie_actual = []
        serie_actual.append(numero_en_estudio)
        numero_evolucion = evolucion(numero_en_estudio)

        elemento = [numero_en_estudio, serie_actual, serie_actual.__len__()]
        tablero.append(elemento)

        fin_de_ciclo = True
        #print(serie_actual.__len__(), " --> ", serie_actual)

print(" Números de Kaprekar para {} cifras ==> ".format(str(cifras)), numeros_de_kaprekar.sort(reverse=False))
