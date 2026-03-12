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
    tirada = 0
    jugar =""

    while jugar != "1":
        jugar = input("Presione 1 para jugar: ")

    dados_actuales = tirada_dados(5)
    tirada += 1

    generala_real = False
    if generala(dados_actuales):
        generala_real = True

    print("Tirada ", tirada, "-> ", dados_actuales)

    if generala_real:
        print("Turno terminado. Dados finales: ", dados_actuales)
        return dados_actuales, tirada, generala_real
    
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
    return dados_actuales, tirada, generala_real

def guardar_planilla_csv(planilla, archivo = "jugadas.csv"):
    orden = ["E", "F", "P", "G", "1", "2", "3", "4", "5", "6"]

    with open(archivo, "w", newline = "", encoding = "utf-8") as f:
        writer =csv.writer(f)
        writer.writerow(["Jugada", "j1", "j2"])

        for cat in orden:
            j1 = planilla[cat][0]
            j2 = planilla[cat][1]

            if j1 is None:
                j1 = 0
            if j2 is None:
                j2 = 0
            
            writer.writerow([cat, j1, j2])

def jugar_partida():
    print("Bienvenido al Juego de la Generala")
    planilla = {}
    for cat in categorias:
        planilla[cat] = [None, None]

    nombres = ["Jugador 1", "Jugador 2"]

    for ronda in range(len(categorias)):
        print("\n")
        print("Ronda", ronda + 1)

        for jugador in [0, 1]:
            print("\nTurno de: ", nombres[jugador])

            dados_finales, tirada, generala_real = turno_generala()

            if generala_real:
                print("\n ¡GENERALA REAL! Gana", nombres[jugador])
                planilla["G"][jugador] = 80
                guardar_planilla_csv(planilla)
                return

            categoria = input("Elegí categoría (1-6, E, F, P, G): ").strip().upper()

            while categoria not in categorias or planilla[categoria][jugador] is not None:
                categoria = input("Categoría inválida. Elegí otra por favor (1-6, E, F, P, G): ").strip().upper()

            puntos = puntaje_categoria(categoria, dados_finales)
            planilla[categoria][jugador] = puntos
            
            guardar_planilla_csv(planilla)

            print("Elegiste ", categoria, "y tu puntaje es: ", puntos)

    print("\nPlanilla: ", planilla)

    total_j1 = 0
    total_j2 = 0

    for cat in categorias:
        total_j1 += planilla[cat] [0]
        total_j2 += planilla[cat] [1]
    print("\n Total Jugador 1: ", total_j1)
    print("Total Jugador 2: ", total_j2)

    if total_j1 > total_j2:
        print("Gana Jugador 1")
    elif total_j2 > total_j1:
        print("Gana Jugador 2")
    else:
        print("Empate")

def main():
        jugar_partida()

if __name__ == "__main__":
    main()






        



        

