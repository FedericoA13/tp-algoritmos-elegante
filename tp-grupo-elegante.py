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
        
def main():
    
    matriz_posiciones_stackeada, matriz_letras_stackeada=matriz_juego()
    mostrar_fichas_posiciones(matriz_posiciones_stackeada,matriz_letras_stackeada)
    
    letras_descubiertas=0
    intentos=0
    
    while letras_descubiertas<int(const.FILAS*const.COLUMNAS/2):
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
        lista_validacion=[x for x in range(1,const.FILAS*const.COLUMNAS+1)]
        
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
            
    print("Felicitaciones. Has encontrado todos los pares de letras. Has ganado.")
    print("Te ha llevado",intentos,"intentos resolver el memotest")
            
main()
