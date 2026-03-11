from random import randint
import csv

categorias = ["1", "2", "3", "4","5", "6", "E", "F", "P", "G"]

def contar_dados(dados):
    conteo = {}
    for d in dados:
        if d in conteo:
            conteo[d] = conteo[d] + 1
        else: 
            conteo[d] = 1
    return conteo
    
def generala(dados):
    d = sorted(dados)
    return d[0] == d[4]

def poker(dados):
    d = sorted(dados)
    return (d[0] == d[3]) or (d[1] == d[4])

def full(dados):
    d = sorted(dados)
    caso1 = (d[0] == d[2]) and (d[3] == d[4]) and (d[2] != d[3])
    caso2 = (d[0] == d[1]) and (d[2] == d[4]) and (d[1] != d[2])
    return caso1 or caso2

def escalera(dados):
    d = sorted(dados)
    return d == [1, 2, 3, 4, 5] or d == [2, 3, 4, 5, 6]

def puntaje_categoria(categoria, dados):

    if categoria in ["1", "2", "3", "4", "5", "6"]:
        n = int(categoria)
        cantidad = dados.count(n)
        puntos = cantidad*n
        return puntos
    if categoria == "E":
        if escalera(dados):
            return 20
        else:
            return 0
    if categoria == "F":
        if full(dados):
            return 30
        else:
            return 0
    if categoria == "P":
        if poker(dados):
            return 40
        else:
            return 0
    if categoria == "G":
        if generala(dados):
            return 50
        else:
            return 0
    
    return 0

def tirada_dados (cantidad):
    dados = []
    for dado in range(0,cantidad):
        dados.append(randint(1,6))
    return dados


def turno_generala():
    print("Bienvenido al Juego de la Generala")
    tirada = 0
    cant_jugadores = 1
    seguir = True
    jugar = ""
    
    while jugar != "1":
        jugar = input("Presione 1 para jugar")

    dados_actuales = tirada_dados(5)
    tirada +=1

    print("Tirada", tirada, "->", dados_actuales)

    while tirada < 3:
        respuesta = input("¿Desea volver a tirar? (s/n): ").strip().lower()

        if respuesta != "s":
            break

        posiciones_txt = input("¿Qué posiciones querés volver a tirar? (1-5, por ejemplo: 1 3 4): ")
        
        posiciones_txt = posiciones_txt.replace(","," ")
        partes = posiciones_txt.split()

        posiciones = []
        for p in partes:
            if p.isdigit():
                n = int(p)
                if 1 <= n <= 5 and n not in posiciones:
                    posiciones.append(n)

        if len(posiciones) == 0:
            break

        for pos in posiciones:
            dados_actuales [pos - 1] = randint(1,6)

        tirada +=1
        print("Tirada", tirada, "->", dados_actuales)
    
    print("Turno terminado. Dados finales: ", dados_actuales)
    return dados_actuales

turno_generala()







        



        

