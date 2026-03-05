from random import randint

def tirada_dados (cantidad):
    dados = []
    for dado in range(0,cantidad):
        dados.append(randint(1,6))
    return dados


def generala(dados,posiciones):
    print("Bienvenido al Juego de la Generala")
    tirada = 0
    cant_jugadores = 1
    seguir = True
    jugar = ""
    
    while jugar != "1":
        jugar = input("Presione 1 para jugar")

    dados_actuales = tirada_dados(5)
    tirada +=1

    print("Dados", dados_actuales)

