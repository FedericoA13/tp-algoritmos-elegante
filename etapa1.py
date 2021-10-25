import random
import constantes as const

posicion1 = [1]
posicion2 = [2]
posicion3 = [3]
posicion4 = [4]

ficha1 = 'X'
ficha2 = 'Z'
tablero = [posicion1, posicion2, posicion3, posicion4]
lista_fichas = ['X', 'Z'] * 2

print("1Fichas y posiciones: ", posicion1, posicion2, posicion3, posicion4)
print("2Fichas y posiciones: ", tablero)

print("Fichas y posiciones: ", posicion1, posicion2, posicion3, posicion4)
pedido1 = input("Primera posicion: ")
while pedido1 != '':
    for posiciones in tablero:
        for ficha in lista_fichas:
            if pedido1 == 'X':
                posicion1 = 'X'
                print(tablero)
                pedido2 = input("Segunda posicion: ")
            else:
                print("No acertaste")
                print(tablero)
                pedido1 = input("Primera posicion: ")

def numero_random():
    return random.randint(0, 1)

veces_letra_1 = 0
veces_letra_2 = 0


for asignacion in range(const.FICHAS_EN_TABLERO):
    asignar = numero_random()
    if asignar == 0 and veces_letra_1 <= 1:
        lista_fichas.append(ficha1)
        veces_letra_1 += 1
    elif asignar == 1 and veces_letra_2 <= 1:
        lista_fichas.append(ficha2)
        veces_letra_2 += 1

print(lista_fichas)

# TODO: Asignar letras a cada posicion de la lista de fichas

'''
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
'''
