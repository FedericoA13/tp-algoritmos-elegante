FILAS=1 #este valor es modificable
COLUMNAS=4 #este valor es fijo
import string
import random
from timeit import default_timer
from tkinter import *

def matriz_juego():
    #creo 1 matriz de numeros que es la que vera el usuario
    matriz_posiciones=[]
    FILAS_COMODIN=int(FILAS/FILAS) #Esto hace que se genere una sola linea que dps se cortara y stackeara 
    for i in range(FILAS_COMODIN):
        matriz_posiciones.append([])
        for j in range(1,FILAS*COLUMNAS+1):
            matriz_posiciones[i].append(j)
    
    #creo una matriz de letras aleatoria
    matriz_letras=[]
    matriz_letras_total=string.ascii_letters
    matriz_letras=random.sample(matriz_letras_total,int(FILAS*COLUMNAS/2))
    matriz_letras=(matriz_letras*2)
    random.shuffle(matriz_letras)
    
    #Agarro la linea de la matriz_posiciones y la la matriz_letra, las corto en partes = y las stackeo cada 1 en su matriz     
    VALOR=4 #quiero que cada fila tenga 4 valores
    if FILAS>1:
        matriz_posiciones_stackeada=[matriz_posiciones[0][x:x+VALOR] for x in range(0,len(matriz_posiciones[0]),VALOR)]
        matriz_letras_stackeada=[matriz_letras[x:x+VALOR] for x in range(0,len(matriz_letras),VALOR)]
    else:
        matriz_posiciones_stackeada=matriz_posiciones
        matriz_letras_stackeada=[matriz_letras]
#     print (matriz_posiciones_split)
#     print (matriz_letras_split)
        
    return matriz_posiciones_stackeada, matriz_letras_stackeada
    
def mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada):
    print("Fichas y Posiciones: ")
    for i in range(int(FILAS)):
        for j in range(int(COLUMNAS)):
            if len(str(matriz_posiciones_stackeada[i][j]))==1:
                print("[ ",str(matriz_posiciones_stackeada[i][j]),"]", end=" ")
            else:
                print("[",str(matriz_posiciones_stackeada[i][j]),"]", end=" ")
        print()
        
    return

def conversor_matriz(matriz):
#convierte 1 matriz con 1 sola fila en una matriz con varias filas que coinciden con el
#parametro FILAS seteado al principio. Y viciversa, convierte una matriz de varias filas en una
#de 1 sola fila
    VALOR=4 #quiero que cada fila tenga 4 valores
    if len(matriz)>1:
        matriz_nueva=[]
        for sublista in matriz:
            for item in sublista:
                matriz_nueva.append(item)
        matriz_nueva=[matriz_nueva]
    else:
        matriz_nueva=[matriz[0][x:x+VALOR] for x in range(0,len(matriz[0]),VALOR)]
        
    return matriz_nueva

def pedir_posiciones(matriz_posiciones_stackeada,contador_posicion):
    validacion_posicion=False
    matriz=conversor_matriz(matriz_posiciones_stackeada)
    
    # se validara que el numero ingresado sea un entero, este en las posiciones mostradas en la
    #pantalla y ademas no haya sido seleccionado antes
    while validacion_posicion==False:
        try:
            if contador_posicion==1:
                posicion=int(input("Ingresa 1ra posicion: "))
            else:
                posicion=int(input("Ingresa 2da posicion: "))
            if 1<=posicion<=(int(FILAS*COLUMNAS)):
                if posicion in matriz[0]:
                    validacion_posicion=True
                else:
                    print("Ha ingresado un valor ya seleccionado antes. Vuelva a ingresar un valor")
                    validacion_posicion=False    
            else:
                print("Ha ingresado un valor fuera del rango permitido. Vuelva a ingresar un valor")
                validacion_posicion=False
        except:
            print("No has ingresado un valor numerico. Vuelve a ingresar un valor")
            validacion_posicion=False
            
    return posicion
        

def solo():
    nombre=nombre_jugadores()
    tiempo_inicial=default_timer()
    matriz_posiciones_stackeada, matriz_letras_stackeada=matriz_juego()
    mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
    
    letras_descubiertas=0
    intentos=0
    contador_posicion=0
    while letras_descubiertas<int(FILAS*COLUMNAS/2):
        posicion1=pedir_posiciones(matriz_posiciones_stackeada,contador_posicion)-1
        #convierto matriz mostrada en pantalla en matriz de 1 fila y asigno operaciones
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        ficha1=matriz_letras_stackeada[0][posicion1]
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        matriz_posiciones_stackeada[0][posicion1]=str(ficha1)
        
        #reconvierto matrices para volver a mostrar en pantalla
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
        
        posicion2=pedir_posiciones(matriz_posiciones_stackeada,contador_posicion)-1
        
        #convierto matriz mostrada en pantalla en matriz de 1 fila y asigno operaciones
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        ficha2=matriz_letras_stackeada[0][posicion2]
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        matriz_posiciones_stackeada[0][posicion2]=str(ficha2)
        
        #reconvierto matrices para volver a mostrar en pantalla
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
        
        #se crea lista que retorna a los valores originales las posiciones que el usuario pidio ver
        lista_validacion=[x for x in range(1,FILAS*COLUMNAS+1)]
        
        if ficha1!=ficha2:
            matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
            matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
            
            matriz_posiciones_stackeada[0][posicion1]=lista_validacion[posicion1]
            matriz_posiciones_stackeada[0][posicion2]=lista_validacion[posicion2]
            
            matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
            matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
            
            print("Las posiciones seleccionadas no tenian la misma letra. Vuelve a intentarlo")
            
            mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
            intentos=intentos+1
        else:
            print("Muy bien. Encontraste un par de letras iguales")
            letras_descubiertas=letras_descubiertas+1
            intentos=intentos+1
    tiempo_final=default_timer()        
    print(f"Felicitaciones {nombre}. Has encontrado todos los pares de letras. Has ganado")
    print("Te ha llevado",intentos,"intentos resolver el memotest")
    print("En un tiempo de",round(tiempo_final-tiempo_inicial,2),"segundos.")

def multijugador():
    jugador_1=nombre_jugadores()
    jugador_2=nombre_jugadores()
    tiempo_inicial=default_timer()
    
    matriz_jugadores=[jugador_1,jugador_2]
    random.shuffle(matriz_jugadores)
    
    turno_jugador_shuffle=matriz_jugadores[0]
    
    print("Comenzara jugando:",turno_jugador_shuffle)
    
    matriz_posiciones_stackeada, matriz_letras_stackeada=matriz_juego()
    mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
    
    letras_descubiertas=0
    intentos_jugador_shuffle_1=0
    intentos_jugador_shuffle_2=0
    letras_descubiertas_jugador_1=0
    letras_descubiertas_jugador_2=0
    intentos_jugador_shuffle=[[intentos_jugador_shuffle_1,letras_descubiertas_jugador_1],[intentos_jugador_shuffle_2,letras_descubiertas_jugador_2]]
    
    while letras_descubiertas<int(FILAS*COLUMNAS/2):
        contador_posicion=1
        posicion1=pedir_posiciones(matriz_posiciones_stackeada,contador_posicion)-1
        
        #convierto matriz mostrada en pantalla en matriz de 1 fila y asigno operaciones
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        ficha1=matriz_letras_stackeada[0][posicion1]
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        matriz_posiciones_stackeada[0][posicion1]=str(ficha1)
        
        #reconvierto matrices para volver a mostrar en pantalla
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
        
        contador_posicion=2
        posicion2=pedir_posiciones(matriz_posiciones_stackeada,contador_posicion)-1
        
        #convierto matriz mostrada en pantalla en matriz de 1 fila y asigno operaciones
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        ficha2=matriz_letras_stackeada[0][posicion2]
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        matriz_posiciones_stackeada[0][posicion2]=str(ficha2)
        
        #reconvierto matrices para volver a mostrar en pantalla
        matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
        matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
        mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
        
        #se crea lista que retorna a los valores originales las posiciones que el usuario pidio ver
        lista_validacion=[x for x in range(1,FILAS*COLUMNAS+1)]
        
        if ficha1!=ficha2:
            matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
            matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
            
            matriz_posiciones_stackeada[0][posicion1]=lista_validacion[posicion1]
            matriz_posiciones_stackeada[0][posicion2]=lista_validacion[posicion2]
            
            matriz_posiciones_stackeada=conversor_matriz(matriz_posiciones_stackeada)
            matriz_letras_stackeada=conversor_matriz(matriz_letras_stackeada)
            
            if turno_jugador_shuffle==matriz_jugadores[0]:
                intentos_jugador_shuffle[0][0]=intentos_jugador_shuffle[0][0]+1
                print("Mala suerte",matriz_jugadores[0],"las posiciones seleccionadas no tenian la misma letra. Le toca jugar a",matriz_jugadores[1])
                turno_jugador_shuffle=matriz_jugadores[1]
            else:
                intentos_jugador_shuffle[1][0]=intentos_jugador_shuffle[1][0]+1
                print("Mala suerte",matriz_jugadores[1],"las posiciones seleccionadas no tenian la misma letra. Le toca jugar a",matriz_jugadores[0])
                turno_jugador_shuffle=matriz_jugadores[0]
            
            mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
        else:
            letras_descubiertas=letras_descubiertas+1
            if letras_descubiertas <(int(FILAS*COLUMNAS/2)):
                if turno_jugador_shuffle==matriz_jugadores[0]:
                    intentos_jugador_shuffle[0][0]=intentos_jugador_shuffle[0][0]+1
                    intentos_jugador_shuffle[0][1]=intentos_jugador_shuffle[0][1]+1
                    print("Muy bien",matriz_jugadores[0],"encontraste un par de letras iguales. Puedes continuar jugando")
                else:
                    intentos_jugador_shuffle[1][0]=intentos_jugador_shuffle[1][0]+1
                    intentos_jugador_shuffle[1][1]=intentos_jugador_shuffle[1][1]+1
                    print("Muy bien",matriz_jugadores[1],"encontraste un par de letras iguales. Puedes continuar jugando")
                
    if turno_jugador_shuffle==matriz_jugadores[0]:
        intentos_jugador_shuffle[0][0]=intentos_jugador_shuffle[0][0]+1
        intentos_jugador_shuffle[0][1]=intentos_jugador_shuffle[0][1]+1
        print("Muy bien",matriz_jugadores[0],"encontraste un par de letras iguales. Ya no quedan mas letras por encontrar")
    else:
        intentos_jugador_shuffle[1][0]=intentos_jugador_shuffle[1][0]+1
        intentos_jugador_shuffle[1][1]=intentos_jugador_shuffle[1][1]+1
        print("Muy bien",matriz_jugadores[1],"encontraste un par de letras iguales. Ya no quedan mas letras por encontrar")
    tiempo_final=default_timer()
    print(f"Felicitaciones. Han encontrado todos los pares de letras.")
    jugadorGanador=ganador(intentos_jugador_shuffle)
    jugadorIntentos=intentos(intentos_jugador_shuffle)
    print(f"El jugador ganador es {matriz_jugadores[jugadorGanador]} con {intentos_jugador_shuffle[jugadorGanador][jugadorIntentos]} intentos\nEn un tiempo de: {round(tiempo_final-tiempo_inicial,2)} segundos ")


def main():
    print("*-*-*-*-*-*-*-BIENVENIDO AL JUEGO DEL MEMOTEST-*-*-*-*-*-*-*")
    cantidad=cantidad_jugadores()
    if cantidad==1:
        solo()
    else:
        multijugador()

def cantidad_jugadores():
    cantidadJugadores=int(input("Ingrese la cantidad de jugadores\n 1- Un jugador:\n 2- Multijugador\n Opcion: "))
    return cantidadJugadores


def nombre_jugadores():
    nombre=str(input("ingrese su nombre: "))
    return nombre
    
def ganador(intentos_jugador_shuffle):
    ganadorintentos=0
    if intentos_jugador_shuffle[0][1]>intentos_jugador_shuffle[1][1]:
        ganadorintentos=0
    elif intentos_jugador_shuffle[0][1]<intentos_jugador_shuffle[1][1]:
        ganadorintentos=1
    else:
        if intentos_jugador_shuffle[0][0]>intentos_jugador_shuffle[1][0]:
            ganadorintentos=0
        else:
            ganadorintentos=1
    return ganadorintentos
            

def intentos(intentos_jugador_shuffle): 
    intentosJugador=0
    if intentos_jugador_shuffle[0][0]>intentos_jugador_shuffle[1][0]:
        intentosJugador=0
    else:
        intentosJugador=1
    return intentosJugador

def interfaz_grafica():
    raiz= Tk()
    raiz.title("Ingreso nombres - Memotest")
    raiz.resizable(False, False)
    raiz.geometry("300x130")
    raiz.config(bg="red")

    miFrame = Frame(raiz, width = 250, height = 120)
    miFrame.pack()

    JugadorLabel = Label(miFrame, text="Nombre jugador:",fg="Blue").place(x = 5, y = 35)
    errorLabel= Label(miFrame)
    errorLabel.place(x=5,y=80)

    jugadorEntry = Entry(miFrame)
    jugadorEntry.place(x = 110, y= 35)

    botonEnviar = Button(miFrame,text="Ingresar",fg="Blue",command=nombre_jugadores).place(x= 50, y = 80)
    botonSalir= Button(miFrame,text="Salir",fg="Blue",command=raiz.quit).place(x= 130, y = 80)

    raiz.mainloop()
         
main()
