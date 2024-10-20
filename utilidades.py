
import numpy as np
import pandas as pd
import math

from generaradores import *
from pruebas import *



def pruebas():
    
    P_media = medias()
    resultado = P_media.probar('archivo.txt')
    print('Prueba_Media: ' , resultado)
    
    P_varianza = varianza()
    resultado = P_varianza.probar('archivo.txt')
    print('Prueba_Varianza: ' , resultado)
    
    P_Chi_Cudrado = chi_cuadrado()
    resultado = P_Chi_Cudrado.probar('archivo.txt')
    print('Prueba_Chi_Cuadrado: ' , resultado)
    
    P_Corrida = corridas_ariba_abajo()
    resultado = P_Corrida.probar('archivo.txt')
    print('Prueba_Corridad_Ariba_Abajo: ' , resultado)
    
    P_Corrida_Media = corridas_ariba_abajo_media()
    resultado = P_Corrida_Media.probar('archivo.txt')
    print('Prueba_Corrida_Media: ' , resultado)
    
    P_Poker = Poker()
    resultado = P_Poker.probar('archivo.txt')
    print('Prueba_Poker: ' , resultado)
    
    
    
    
    
############################################################################### 
# NO CONGRUENCIALES CUADRADOS MEDIOS  
# PERIODO = 27
# SEMILLA = 5735
# INICIO 0,8902 0,2456
# FIN 0.1000 0,0000 

def No_Congruencial_Cuadrados_Medios():
    generador = Cuadrados_Medios() 
    semilla_inicial = str(input("Introduce la semilla inicial (número): "))
    
    x = [] # Historico Semillas
    r = [] # Ri

    for i in range(10000000):

        if semilla_inicial in x:  
            print("#####################################")
            print('Cantidad de Ri Guardados :',i - 1)
            print("#####################################")
            indice = x.index(semilla_inicial)
            #print('Índice encontrado:', indice)
            break
        else:
            x.append(semilla_inicial)

        R, semilla_inicial = generador.generar(semilla_inicial)
        r.append(str(R))
        
        

    r.pop() #Elimino la ultima semilla r porque hago un guardado extra
    
    
    
    # Convertir la lista de diccionarios a un DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    #print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
   
    with open(nombre_archivo, 'w') as archivo:
     # Convertir cada float a string y unirlos con un espacio
     contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
     # Escribir la cadena en el archivo
     archivo.write(contenido)
     
    #print(r)
    
#################################################################################

    
#SEMILLA (X1=5015  X2=5734)
#CANTIDAD DE PERIODO (186 629)
#FIN  0.1500,0.6500,0.7500,0.7500,0.2500,0.7500,0.7500
def No_Congruencial_Productos_Medios():
    generador = Productos_Medios()

    x =[]
    r = []
    
    semilla1 = str(input("Introduce la semilla 1 (número): "))
    semilla2 = str(input("Introduce la semilla 2 (número): "))

    for i in range(10000000):
        
        tupla = (semilla1,semilla2)
        if(tupla in x):
            print("#####################################")
            print('Cantidad de Ri Guardados :',i - 1)
            print("#####################################")
            indice = x.index(tupla)
            #print('Índice encontrado:', indice)
            break
        else:
             x.append(tupla)

        R, new_semilla = generador.generar(semilla1, semilla2)
        r.append(str(R))

        semilla1 = str(semilla2)
        semilla2 = str(new_semilla)
        
    
    r.pop()
    # Convertir la lista de diccionarios a un DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    #print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
    with open(nombre_archivo, 'w') as archivo:
     # Convertir cada float a string y unirlos con un espacio
     contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
     # Escribir la cadena en el archivo
     archivo.write(contenido)
     
    #print(r)
    
#========================================================================================#
    
    
    
    
    
    

#SEMILLA 9803
#A constante = 6965
#INICIA = 0.2778
#TERMINA = 

def No_Congruencial_Multiplicador_Constante():
    x = []
    r = []
    
    semilla_inicial = str(input("Introduce la semilla 1 (número): "))
    a = int(input("Introduce la constante (a): "))
    
    #Instanciamos la clase
    generador = Multiplicador_Constante(a)
    
    
    for i in range(1000000):
        if  semilla_inicial in x:
            print("#####################################")
            print('Cantidad de Ri Guardados :',i - 1)
            print("#####################################")
            indice = x.index(semilla_inicial)
            #print('Índice encontrado:', indice)
            break
        else:
            x.append(semilla_inicial)
        
        
        R,New_Semilla = generador.generar(semilla_inicial)
        semilla_inicial = str(New_Semilla)
        r.append(str(R))
        
    r.pop()

    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    #print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
    with open(nombre_archivo, 'w') as archivo:
        # Convertir cada float a string y unirlos con un espacio
        contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
        # Escribir la cadena en el archivo
        archivo.write(contenido)
        
              
    
    
    
    


#====================================================================#
# X0 =37  A = 19 C=33 M = 100
#PERIDODO 10 
#INICIO 0.36363636363636365 0.171717171717171
#FIN  0.5757575757575758 0.16161616161616163 0.37373737373737376


def Congruencial_Lineal():
    # Parámetros de ejemplo
    semilla_inicial = str(input("Introduce la semilla 1 (número): "))
    
    a = int(input("Introduce  (a): "))
    c = int(input("Introduce  (c): "))
    m = int(input("Introduce  (m): "))
    
    x = []
    r = []

    #Instanciamos la clase
    generador = congruencial_lineal(a, c, m)
    
    
    for i in range(1000000):
        if  semilla_inicial in x:
            print("#####################################")
            print('Cantidad de Ri Guardados :',i )
            print("#####################################")
            indice = x.index(semilla_inicial)
            #print('Índice encontrado:', indice)
            break
        else:
            x.append(semilla_inicial)
        
        
        R,New_Semilla = generador.generar(semilla_inicial)
        semilla_inicial = str(New_Semilla)
        r.append(str(R))
        
        
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    #print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
    with open(nombre_archivo, 'w') as archivo:
        # Convertir cada float a string y unirlos con un espacio
        contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
        # Escribir la cadena en el archivo
        archivo.write(contenido)
        
#====================================================================#



def Congruencial_Multiplicativo():
   
    semilla_inicial = int(input("Introduce (semilla)): "))
    
    a = int(input("Introduce  (a): "))
    m = int(input("Introduce  (m): "))
    
    x = []
    r = []
    generador = congruencial_multiplicativo(a, m)
    
    # Generar los números pseudoaleatorios
    for i in range(1000000):
        if semilla_inicial in x:  # Detener si la semilla se repite
            print("#####################################")
            print('Cantidad de Ri Guardados :',i )
            indice = x.index(semilla_inicial)
            print("#####################################")
            break
        else:
            x.append(semilla_inicial)
        
        # Generar el siguiente número y actualizar la semilla
        R, new_semilla = generador.generar(semilla_inicial)
        semilla_inicial = new_semilla  # Actualizar la semilla inicial para la próxima iteración
        r.append(str(round(R, 5)))

    # Crear DataFrame para visualizar los datos generados
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    #print(df)
    
    # Guardar los resultados en un archivo de texto
    nombre_archivo = "archivo.txt"
    with open(nombre_archivo, 'w') as archivo:
        contenido = ' '.join(r)
        archivo.write(contenido)
        
#===========================================================================================#

 
 
 
 
 
 
def Congruencial_Aditivo():
    
    n = int(input("Cuantos valores tiene la semilla: "))
    semilla_inicial = []
    
    for i in range(n):
        sem = int(input("Introduce  semilla : "))
        semilla_inicial.append(sem)
        
    
    
    m = int(input("Introduce  (m): "))
    

    
    x = []
    r = []
    generador = congruencial_aditivo(m)
    
    for i in range(100000):
        
        if tuple(semilla_inicial) in x:
            print("#####################################")
            print('Cantidad de Ri Guardados :',i-1 )
            
            print("#####################################")
            break
        else:
            x.append(tuple(semilla_inicial))
        
        R, New_Semilla = generador.generar(semilla_inicial)
        
        # Añadir nueva semilla a la lista, eliminando el primer elemento
        semilla_inicial = semilla_inicial[1:] + [New_Semilla]
        r.append(str(round(R, 5)))
        
    r.pop()
    # Crear DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    #print(df)
    
    # Crear archivo TXT
    nombre_archivo = "archivo.txt"
    with open(nombre_archivo, 'w') as archivo:
        contenido = ' '.join(r)
        archivo.write(contenido)
        
    print('-----------------GENERANDO TXT CON ÉXITO---------------------------')

    
        
        
#periodo 8
#semilla 13 m 8 a 26 b 27 c 27     
def Congruencial_Cuadratico():
   
    
    
    semilla_inicial = int(input("Introduce (semilla)): "))
    
    a = int(input("Introduce  (a): "))
    b = int(input("Introduce  (b): "))
    c = int(input("Introduce  (c): "))
    m = int(input("Introduce  (m): "))
    
    
    x = []
    r = []
    generador = congruencial_cuadratico(a, b, c, m)
    
    for i in range(1000000):
        if semilla_inicial in x:
            print("#####################################")
            print('Cantidad de Ri Guardados :',i - 1 )
            print("#####################################")
            break
        else:
            x.append(semilla_inicial)
        
        R, new_semilla = generador.generar(semilla_inicial)
        semilla_inicial = new_semilla  # Mantenemos semilla_inicial como un entero
    
        r.append(str(R))
        
        
       
    r.pop()###########################
    # Crear DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    #print(df)
    
    # Crear archivo TXT
    nombre_archivo = "archivo.txt"
    with open(nombre_archivo, 'w') as archivo:
        contenido = ' '.join(r)
        archivo.write(contenido)
        
    print('-----------------GENERANDO TXT CON ÉXITO---------------------------')




def G_blum():
    # Entrada de datos
    semilla_inicial = int(input("Introduce la semilla inicial: "))
    p = int(input("Introduce el valor de p: "))
    q = int(input("Introduce el valor de q: "))

    # Listas para guardar los valores de las semillas y Ri
    x = []
    r = []

    # Crear la instancia de la clase Blum
    generador = blum(p, q)

    for i in range(1000000):
        if semilla_inicial in x:
            print("#####################################")
            print('Cantidad de Ri Guardados:', i-1)
            print("#####################################")
            break
        else:
            x.append(semilla_inicial)

        R, new_semilla = generador.generar(semilla_inicial)
        semilla_inicial = new_semilla  # Actualizamos la semilla para la siguiente iteración
    
        r.append(str(R))
        
    # Elimina el último valor de r
    if r:
        r.pop()

    # Crear DataFrame con los datos generados
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    print(df)  # Si quieres visualizar los datos generados
    
        
    
       
#FIN DE FUNCIONES      
             
             
             
             
             
#INICIO DE MENU

def generar_periodo():
    while True:
        print("\nMenú de Opciones:")
        print("1. Opción 1 - Generar No Congruencial Cuadrados Medios")
        print("2. Opción 2 - Generar No Congruencial Multiplicador Constante") #PARAMETROS A
        print("3. Opción 3 - Generar No Congruencial Productos Medios")
        
        print("4. Opción 4 - Generar Congruenial lineal")#PARAMETROS A C M
        print("5. Opción 5 - Generar Congruenial multiplicativo") # PARAMETROS A M
        print("6. Opción 6 - Generar Congruenial aditivo") # M
        print("7. Opción 7 - Generar Congruenial cuadratico")# A B C M
        
        print("9. Salir")

        opcion = input("Selecciona una opción (1-7): ")
        
    

        if opcion == '1':
            No_Congruencial_Cuadrados_Medios() #ACTIVO
            pruebas()
        elif opcion == '2':
            No_Congruencial_Multiplicador_Constante()#ACTIVO
            pruebas()
        elif opcion == '3':
            No_Congruencial_Productos_Medios() #ACTIVO
            pruebas()
        elif opcion == '4':
            Congruencial_Lineal() #ACTIVO
            pruebas()
        elif opcion == '5':
            Congruencial_Multiplicativo()
            pruebas()
        elif opcion == '6':
            Congruencial_Aditivo()
            pruebas()
        elif opcion == '7':
            Congruencial_Cuadratico()
            pruebas()
        elif opcion == '8':
            G_blum()
            
        elif opcion == '9':
            print("Saliendo del programa...")
            break  # Salir del bucle y del programa

        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Llamar a la función para iniciar el menú
generar_periodo()








    
    
    
    
    
    
