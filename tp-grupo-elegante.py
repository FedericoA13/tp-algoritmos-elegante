import constantes as const
import string
import random

def matriz_juego():
    #creo 1 matriz de numeros que es la que vera el usuario
    matriz_posiciones=[]
    for i in range(1,int(const.FILAS*const.COLUMNAS+1)):
        matriz_posiciones.append(i)

    #creo una matriz de letras aleatoria
    matriz_letras=[]
    matriz_letras_total=string.ascii_letters
    matriz_letras=random.sample(matriz_letras_total,int(const.FILAS*const.COLUMNAS/2))
    matriz_letras=(matriz_letras*2)
    random.shuffle(matriz_letras)
    
    #Agarro la matriz_posiciones y la matriz_letras, las corto en partes = y las apilo cada 1 en su matriz     
    if const.FILAS>1:
        matriz_posiciones_apiladas=[matriz_posiciones[x:x+const.VALOR] for x in range(0,len(matriz_posiciones),const.VALOR)]
        matriz_letras_apiladas=[matriz_letras[x:x+const.VALOR] for x in range(0,len(matriz_letras),const.VALOR)]
    else:
        matriz_posiciones_apiladas=[matriz_posiciones]
        matriz_letras_apiladas=[matriz_letras]
        
    return matriz_posiciones_apiladas, matriz_letras_apiladas
    
def mostrar_fichas_posiciones(matriz_posiciones_apiladas):
    #esta funcion convierte la matriz_posiciones_apiladas en su version para ser impresa en pantalla
    print("Fichas y Posiciones: ")
    for i in range(int(const.FILAS)):
        for j in range(int(const.COLUMNAS)):
            #si el numero de posicion en la matriz es < 10 necesita agregarle un espacio para que los numeros queden bien alineados en la matriz impresa
            if len(str(matriz_posiciones_apiladas[i][j]))==1:
                print("[ ",str(matriz_posiciones_apiladas[i][j]),"]", end=" ")
            else:
                print("[",str(matriz_posiciones_apiladas[i][j]),"]", end=" ")
        print()
        
    return

def conversor_matriz(matriz):
#esta funcion convierte 1 matriz con 1 sola fila en una matriz con varias filas que coinciden con el
#parametro FILAS seteado al principio. Y viciversa, convierte una matriz de varias filas en una
#de 1 sola fila
    if len(matriz)>1:
        matriz_nueva=[]
        for sublista in matriz:
            for item in sublista:
                matriz_nueva.append(item)
        matriz_nueva=[matriz_nueva]
    else:
        matriz_nueva=[matriz[0][x:x+const.VALOR] for x in range(0,len(matriz[0]),const.VALOR)]
        
    return matriz_nueva

def pedir_validar_posiciones(matriz_posiciones_apiladas,contador_posicion):
    validacion_posicion=False
    matriz_a_chequear=conversor_matriz(matriz_posiciones_apiladas)
    
    #esta funcion validara que el numero ingresado sea un entero, este en las posiciones mostradas en la
    #pantalla y ademas no haya sido seleccionado antes
    while not validacion_posicion:
        try:
            if contador_posicion==1:
                posicion=int(input("Ingrese 1ra posicion: "))
            else:
                posicion=int(input("Ingrese 2da posicion: "))
            if 1<=posicion<=(int(const.FILAS*const.COLUMNAS)):
                if posicion in matriz_a_chequear[0]:
                    validacion_posicion=True
                else:
                    print("Ingresaste un valor ya seleccionado antes. Volve a ingresar otro valor")
                    validacion_posicion=False    
            else:
                print("Ingresaste un valor fuera del rango permitido. Solo podes ingresar los valores que ves en pantalla. Volve a ingresar otro valor")
                validacion_posicion=False
        except:
            print("Ingresaste un valor o caracter no permitido. Solo podes ingresar los valores que ves en pantalla. Vuelve a ingresar otro valor")
            validacion_posicion=False
            
    return posicion

def buscar_reemplazar_posiciones(matriz_posiciones_apiladas,matriz_letras_apiladas,posicion):
    #esta funcion reemplaza el valor que se ve en la pantalla de la posicion con la letra que esta oculta en esa misma posicion
    
    #convierto las matrices de posiciones y letras en matrices de 1 sola fila para facilitar operaciones de buscar y encontrar numeros/letras 
    matriz_letras_apiladas=conversor_matriz(matriz_letras_apiladas)
    ficha=matriz_letras_apiladas[0][posicion]
    matriz_posiciones_apiladas=conversor_matriz(matriz_posiciones_apiladas)
    matriz_posiciones_apiladas[0][posicion]=str(ficha)
    
    #reconvierto matrices para que se muestren correctamente en pantalla
    matriz_letras_apiladas=conversor_matriz(matriz_letras_apiladas)
    matriz_posiciones_apiladas=conversor_matriz(matriz_posiciones_apiladas)
    
    return ficha, matriz_posiciones_apiladas, matriz_letras_apiladas
    
def resetear_matriz_posiciones(matriz_posiciones_apiladas,matriz_letras_apiladas,posicion1,posicion2):
    #si el jugador no acierta la letra con las fichas escogidas esta funcion resetea los valores de la matriz de posiciones
    #a la posicion que ocupaba la letra (es la inversa de la funcion buscar_reemplazar_posiciones)
    
    #creo lista con numeros que son los que van a reemplazar a las letras (notar que tiene el mismo orden que la matriz_posiciones_apiladas)
    lista_validacion=[x for x in range(1,FILAS*COLUMNAS+1)]
    
    matriz_posiciones_apiladas=conversor_matriz(matriz_posiciones_apiladas)
    matriz_letras_apiladas=conversor_matriz(matriz_letras_apiladas)
            
    matriz_posiciones_apiladas[0][posicion1]=lista_validacion[posicion1]
    matriz_posiciones_apiladas[0][posicion2]=lista_validacion[posicion2]
            
    matriz_posiciones_apiladas=conversor_matriz(matriz_posiciones_apiladas)
    matriz_letras_apiladas=conversor_matriz(matriz_letras_apiladas)
    
    return matriz_posiciones_apiladas, matriz_letras_apiladas

def ganador_memotest(lista_intentos_letras_descubiertas,matriz_jugadores):
    #esta funcion devuelve al ganador del juego si hubo uno o muestra empate
    if lista_intentos_letras_descubiertas[0][1]>lista_intentos_letras_descubiertas[1][1]:
        resultado=print("El ganador de la partida es {} con {} pares de fichas encontradas".format(matriz_jugadores[0],lista_intentos_letras_descubiertas[0][1]))
    elif lista_intentos_letras_descubiertas[0][1]<lista_intentos_letras_descubiertas[1][1]:
        resultado=print("El ganador de la partida es {} con {} pares de fichas encontradas".format(matriz_jugadores[1],lista_intentos_letras_descubiertas[1][1]))
    else:
        if lista_intentos_letras_descubiertas[0][0]<lista_intentos_letras_descubiertas[1][0]:
            resultado=print ("El ganador de la partida es {}. Ambos encontraron {} pares de fichas pero {} lo hizo en menos intentos".format(matriz_jugadores[0],lista_intentos_letras_descubiertas[0][1],matriz_jugadores[0]))
        elif lista_intentos_letras_descubiertas[0][0]>lista_intentos_letras_descubiertas[1][0]:
            resultado=print ("El ganador de la partida es {}. Ambos encontraron {} pares de fichas pero {} lo hizo en menos intentos".format(matriz_jugadores[1],lista_intentos_letras_descubiertas[1][1],matriz_jugadores[1]))
        else:
            resultado=print("El juego termino en empate. Ambos encontraron {} pares de fichas en {} intentos".format(int(lista_intentos_letras_descubiertas[0][0]/2),lista_intentos_letras_descubiertas[0][1]))
    
    return resultado

def main():
    
    print("Bienvenido al juego del Memotest")
    jugador_1=str(input("Jugador 1, ingrese su nombre: "))
    jugador_2=str(input("Jugador 2, ingrese su nombre: "))
    matriz_jugadores=[jugador_1,jugador_2]
    random.shuffle(matriz_jugadores)
    turno_jugador_shuffle=matriz_jugadores[0]
    
    print("Comenzara jugando:",turno_jugador_shuffle)
    
    matriz_posiciones_apiladas, matriz_letras_apiladas=matriz_juego()
    mostrar_fichas_posiciones(matriz_posiciones_apiladas)
    
    letras_descubiertas=0
    intentos_jugador_shuffle_1=0
    intentos_jugador_shuffle_2=0
    letras_descubiertas_jugador_1=0
    letras_descubiertas_jugador_2=0
    lista_intentos_letras_descubiertas=[[intentos_jugador_shuffle_1,letras_descubiertas_jugador_1],[intentos_jugador_shuffle_2,letras_descubiertas_jugador_2]]
    
    while letras_descubiertas<int(FILAS*COLUMNAS/2):
        contador_posicion=1
        posicion1=pedir_validar_posiciones(matriz_posiciones_apiladas,contador_posicion)-1
        ficha1, matriz_posiciones_apiladas, matriz_letras_apiladas = buscar_reemplazar_posiciones(matriz_posiciones_apiladas,matriz_letras_apiladas,posicion1)
        mostrar_fichas_posiciones(matriz_posiciones_apiladas)
        
        contador_posicion=2
        posicion2=pedir_validar_posiciones(matriz_posiciones_apiladas,contador_posicion)-1
        ficha2, matriz_posiciones_apiladas, matriz_letras_apiladas = buscar_reemplazar_posiciones(matriz_posiciones_apiladas,matriz_letras_apiladas,posicion2)
        mostrar_fichas_posiciones(matriz_posiciones_apiladas)
        
        if ficha1!=ficha2:
            matriz_posiciones_apiladas, matriz_letras_apiladas = resetear_matriz_posiciones(matriz_posiciones_apiladas,matriz_letras_apiladas,posicion1,posicion2)
        
            if turno_jugador_shuffle==matriz_jugadores[0]:
                lista_intentos_letras_descubiertas[0][0]+=1
                print("Mala suerte",matriz_jugadores[0],"las posiciones seleccionadas no tenian la misma letra. Le toca jugar a",matriz_jugadores[1])
                turno_jugador_shuffle=matriz_jugadores[1]
            else:
                lista_intentos_letras_descubiertas[1][0]+=1
                print("Mala suerte",matriz_jugadores[1],"las posiciones seleccionadas no tenian la misma letra. Le toca jugar a",matriz_jugadores[0])
                turno_jugador_shuffle=matriz_jugadores[0]
            
            mostrar_fichas_posiciones(matriz_posiciones_apiladas)
        else:
            letras_descubiertas+=1
            if letras_descubiertas<int(FILAS*COLUMNAS/2):
                if turno_jugador_shuffle==matriz_jugadores[0]:
                    lista_intentos_letras_descubiertas[0][0]+=1
                    lista_intentos_letras_descubiertas[0][1]+=1
                    print("Muy bien",matriz_jugadores[0],"encontraste un par de letras iguales. Puedes continuar jugando")
                else:
                    lista_intentos_letras_descubiertas[1][0]+=1
                    lista_intentos_letras_descubiertas[1][1]+=1
                    print("Muy bien",matriz_jugadores[1],"encontraste un par de letras iguales. Puedes continuar jugando")
    
    if turno_jugador_shuffle==matriz_jugadores[0]:
        lista_intentos_letras_descubiertas[0][0]+=1
        lista_intentos_letras_descubiertas[0][1]+=1
        print("Muy bien",matriz_jugadores[0],"encontraste un par de letras iguales. Ya no quedan mas letras por encontrar")
    else:
        lista_intentos_letras_descubiertas[1][0]+=1
        lista_intentos_letras_descubiertas[1][1]+=1
        print("Muy bien",matriz_jugadores[1],"encontraste un par de letras iguales. Ya no quedan mas letras por encontrar")
    
    print("Felicitaciones. El juego ha terminado")
    ganador_memotest(lista_intentos_letras_descubiertas,matriz_jugadores)
    
main()
