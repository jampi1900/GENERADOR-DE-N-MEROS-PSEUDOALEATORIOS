
import numpy as np
import pandas as pd
import math

from generar import Productos_Medios
from generar import Cuadrados_Medios
from generar import congruencial_lineal
from generar import Multiplicador_Constante
from generar import congruencial_aditivo
from generar import congruencial_cuadratico
from generar import congruencial_multiplicativo
from pruebas import medias


def pruebas():
    prueba = medias()
    resultado = prueba.probar('archivo.txt')
    print('Resultado: ' , resultado)


def No_Congruencial_Cuadrados_Medios():
    generador = Cuadrados_Medios()
    semilla_inicial = str(input("Introduce la semilla inicial (número): "))
    x = []
    r = []

    for i in range(1000):

        if semilla_inicial in x:
            print('-----------------Peridodo Finalizado Cuadrados Medios',i,'---------------------------')
            indice = x.index(semilla_inicial)
            print('Índice encontrado:', indice)
            break
        else:
            x.append(semilla_inicial)

        R, semilla_inicial = generador.generar(semilla_inicial)
        r.append(str(R))


    # Convertir la lista de diccionarios a un DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
   
    with open(nombre_archivo, 'w') as archivo:
     # Convertir cada float a string y unirlos con un espacio
     contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
     # Escribir la cadena en el archivo
     archivo.write(contenido)
     
    #print(r)
    
    
    print('1-----------------GERANDONDO TXT CON EXITO---------------------------')

      
      
def No_Congruencial_Productos_Medios():
    generador = Productos_Medios()

    x =[]
    r = []
    semilla1 = str(input("Introduce la semilla 1 (número): "))
    semilla2 = str(input("Introduce la semilla 2 (número): "))

    for i in range(1000):
        tupla = (semilla1,semilla2)
        if(tupla in x):
            print('-----------------Peridodo Finalizado Prodcutos Medios',i,'---------------------------')
            indice = x.index(tupla)
            print('Índice encontrado:', indice)
            break
        else:
             x.append(tupla)

        R, new_semilla = generador.generar(semilla1, semilla2)
        r.append(str(R))

        semilla1 = str(semilla2)
        semilla2 = str(new_semilla)
        

    # Convertir la lista de diccionarios a un DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
    with open(nombre_archivo, 'w') as archivo:
     # Convertir cada float a string y unirlos con un espacio
     contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
     # Escribir la cadena en el archivo
     archivo.write(contenido)
     
    #print(r)
    
    
    print('3-----------------GERANDONDO TXT CON EXITO---------------------------')
    
    
def Congruencial_Lineal():
    # Parámetros de ejemplo
    semilla_inicial = str(input("Introduce la semilla 1 (número): "))
    a = 19  # Constante multiplicativa
    c = 33  # Constante aditiva
    m = 100  # Módulo

    x = []
    r = []

    #Instanciamos la clase
    generador = congruencial_lineal(a, c, m)
    
    
    for i in range(1000):
        if  semilla_inicial in x:
             break
        else:
            x.append(semilla_inicial)
        
        
        R,New_Semilla = generador.generar(semilla_inicial)
        semilla_inicial = str(New_Semilla)
        r.append(str(R))
        
        
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
    with open(nombre_archivo, 'w') as archivo:
        # Convertir cada float a string y unirlos con un espacio
        contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
        # Escribir la cadena en el archivo
        archivo.write(contenido)
        
    print('-----------------GERANDONDO TXT CON EXITO---------------------------')
     

def No_Congruencial_Multiplicador_Constante():
    x = []
    r = []
    
    semilla_inicial = str(input("Introduce la semilla 1 (número): "))
    a = int(input("Introduce la constante (a): "))
    
    #Instanciamos la clase
    generador = Multiplicador_Constante(a)
    
    
    for i in range(1000):
        if  semilla_inicial in x:
             break
        else:
            x.append(semilla_inicial)
        
        
        R,New_Semilla = generador.generar(semilla_inicial)
        semilla_inicial = str(New_Semilla)
        r.append(str(round(R, 5)))

    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    print(df)
    #Creando TXT
    nombre_archivo = "archivo.txt"
    # Crear o abrir el archivo en modo de escritura
    with open(nombre_archivo, 'w') as archivo:
        # Convertir cada float a string y unirlos con un espacio
        contenido = ' '.join(map(str, r))  # Usar map para convertir cada float a string
        # Escribir la cadena en el archivo
        archivo.write(contenido)
        
    print('-----------------GERANDONDO TXT CON EXITO---------------------------')
            
    
    

        

def Congruencial_Multiplicativo():
    semilla_inicial = 12
    a = 21
    m = 32

    x = []
    r = []
    generador = congruencial_multiplicativo(a, m)
    
    # Generar los números pseudoaleatorios
    for i in range(1000):
        if semilla_inicial in x:  # Detener si la semilla se repite
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
    print(df)
    
    # Guardar los resultados en un archivo de texto
    nombre_archivo = "archivo.txt"
    with open(nombre_archivo, 'w') as archivo:
        contenido = ' '.join(r)
        archivo.write(contenido)
        
    print('-----------------GENERANDO TXT CON ÉXITO---------------------------')

 
 
 
 
 
 
def Congruencial_Aditivo():
    semilla_inicial = [65, 89, 98, 3, 69]  # Semillas iniciales
    n = len(semilla_inicial)
    m = 100  # Módulo
    x = []
    r = []
    generador = congruencial_aditivo(m)
    
    for i in range(1000):
        if tuple(semilla_inicial) in x:
            break
        else:
            x.append(tuple(semilla_inicial))
        
        R, New_Semilla = generador.generar(semilla_inicial)
        
        # Añadir nueva semilla a la lista, eliminando el primer elemento
        semilla_inicial = semilla_inicial[1:] + [New_Semilla]
        r.append(str(round(R, 5)))

    # Crear DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    print(df)
    
    # Crear archivo TXT
    nombre_archivo = "archivo.txt"
    with open(nombre_archivo, 'w') as archivo:
        contenido = ' '.join(r)
        archivo.write(contenido)
        
    print('-----------------GENERANDO TXT CON ÉXITO---------------------------')

    
        
        
    
def Congruencial_Cuadratico():
    semilla_inicial = 13
    a = 26
    b = 27
    c = 27
    m = 8
    
    x = []
    r = []
    generador = congruencial_cuadratico(a, b, c, m)
    
    for i in range(1000):
        if semilla_inicial in x:
            break
        else:
            x.append(semilla_inicial)
        
        R, new_semilla = generador.generar(semilla_inicial)
        semilla_inicial = new_semilla  # Mantenemos semilla_inicial como un entero
        r.append(str(round(R, 5)))

    # Crear DataFrame
    df = pd.DataFrame(generador.data)
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    print(df)
    
    # Crear archivo TXT
    nombre_archivo = "archivo.txt"
    with open(nombre_archivo, 'w') as archivo:
        contenido = ' '.join(r)
        archivo.write(contenido)
        
    print('-----------------GENERANDO TXT CON ÉXITO---------------------------')

        
    
       
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
        
        print("8. Salir")

        opcion = input("Selecciona una opción (1-3): ")
        
    

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
            print("Saliendo del programa...")
            break  # Salir del bucle y del programa

        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Llamar a la función para iniciar el menú
generar_periodo()








    
    
    
    
    
    
