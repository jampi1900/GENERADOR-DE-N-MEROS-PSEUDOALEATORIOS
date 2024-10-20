
import numpy as np
import math
import pandas as pd
from scipy.stats import chi2
from scipy.stats import norm


#PRUEBA DE MEDIAS
class medias:
    def __init__(self,):
         self.Error_Aceptado = 0.05
         self.data = []

    def probar(self, archivo):
        
        # 1.- Primero Obtenemos los Numeros Aleatorios
        with open(archivo, 'r') as file:
            contenido = file.read()
        datos = [float(valor) for valor in contenido.split()]
        #Fin de Lectura
        
        # 2.- Segundo Contamos los numeros
        n = len(datos)
        #Fin de Conteo
        
        # 3.- Calcular la media
        media = np.mean(datos)
        #Fin de la media
  
        # 4.- Calcular los Limintes de Aceptacion
        z_alpha_2_medios = abs(norm.ppf(self.Error_Aceptado/2))
        
        LI = 0.5 - (z_alpha_2_medios) * ( 1 / (math.sqrt(12*n)))
        LS = 0.5 + (z_alpha_2_medios) * ( 1 / (math.sqrt(12*n)))
        
        # 5.- Mostramos todos los datos si es nesesario
        self.data.append({
            'Cantidad de Datos': n,
            'Media:':media,
            'LI':LI,
            'LS':LS,
            'Z(x/2)':z_alpha_2_medios
            
        })
        
        # 6.-Comprobar si se encuentra dentro del rango establecido por los limites
        return LI <= media <= LS
    
#FIN DE PRUEBAS DE MEDIAS  



#PRUEBA DE VARIANZA
class varianza:
    def __init__(self,):
         self.Error_Aceptado = 0.05
         self.data = []

    def probar(self, archivo):
        
        # 1.- Primero Obtenemos los Numeros Aleatorios
        with open(archivo, 'r') as file:
            contenido = file.read()
        datos = [float(valor) for valor in contenido.split()]
        #Fin de Lectura
        
        # 2.- Segundo Contamos los numeros
        n = len(datos)
        #Fin de Conteo
        
        # 3.- Calcular la media
        var = np.var(datos)
        #Fin de la media
  
        # 4.- Calcular los Limintes de Aceptacion
        
        LI = chi2.ppf(abs(self.Error_Aceptado/2),n-1) /  (12*(n-1))
        LS = chi2.ppf(abs(1-(self.Error_Aceptado/2)),n-1) /  (12*(n-1))
        
        # 5.- Mostramos todos los datos si es nesesario
        self.data.append({
            'Cantidad de Datos': n,
            'Varianza:':var,
            'LI':LI,
            'LS':LS,
            
        })
        
        # 6.-Comprobar si se encuentra dentro del rango establecido por los limites
        return LI <= var <= LS
    
#FIN DE PRUEBAS DE VARIANZA




#PRUEBA DE DISTRIBUCION UNIFORME (UNIFORMIDAD - PRUEBA CHI CUADRADA)
class chi_cuadrado:
    def __init__(self):
         self.Error_Aceptado = 0.05
         self.m = 6 #POR DEFECTO 10 INTERVALOS PERO PUEDE CAMBIAR
         self.data = []
         

    def probar(self, archivo):
        
        # 1.- Primero Obtenemos los Numeros Aleatorios
        with open(archivo, 'r') as file:
            contenido = file.read()
        datos = [float(valor) for valor in contenido.split()]
        #Fin de Lectura
        
        # 2.- Segundo Contamos los numeros
        n = len(datos)
        
        #Fin de Conteo
        
        # 3.- Calcular la prueba chi cuadrado 
        chi_cuadrado = chi2.ppf((1 - 0.05),(self.m - 1))
        #Fin de la chi cuadrado
        
        # 4.- Crear tabla intervalos , observado , esperado , sumatoria (e-o)2/e
        E = n / self.m
        
        limites = np.linspace(0.0, 1.0, self.m + 1)
        
        intervalos = pd.cut(datos, bins=limites, right=True)
        
        count_intervalos = intervalos.value_counts().sort_index()

        # Crear un DataFrame para almacenar los resultados
        resultados = pd.DataFrame({
            'Intervalo': count_intervalos.index,
            'Oi': count_intervalos.values,
            'Ei': E
        })
        
        resultados['(Ei - Oi)**2 / Ei'] = ((resultados['Ei'] - resultados['Oi']) ** 2) / resultados['Ei']

        L = sum(resultados['(Ei - Oi)**2 / Ei'])
        
        print(chi_cuadrado,L,resultados)
        
        return L < chi_cuadrado
                
#FIN DE PRUEBAS DE CHI CUADRADO

objeto = chi_cuadrado()
objeto.probar('chi_cuadrado.txt')







#PRUEBA INDEPENDENCIA (PRUEBA DE CORRIDAD ARIBA Y ABAJO)
class corridas_ariba_abajo:
    def __init__(self):
         self.Error_Aceptado = 0.05
         self.data = []
         

    def probar(self, archivo):
        
        # 1.- Primero Obtenemos los Numeros Aleatorios
        with open(archivo, 'r') as file:
            contenido = file.read()
        datos = [float(valor) for valor in contenido.split()]
        #Fin de Lectura
        
        # 2.- Segundo Contamos los numeros
        n = len(datos)
        
        # 3.-Conteno de ceros y unos
        lista =[]
        for i in range(n-1):
            if(datos[i+1]>datos[i]):
                lista.append(1)
            else:
                lista.append(0)
            
        #print(lista)
        
        Co = 1
    
        for i in range(len(lista)-1):
            if( lista[i+1] != lista[i]):
                Co = Co + 1
            else:
                Co = Co
                
                
        #print(Co)
        
        
        #Fin de Conteo
        Uco = ((2 * n) - 1 )/3
        O2_co = ((16*n)-29)/90
        Oco = math.sqrt(O2_co)
        Zo = abs((Co -Uco)/Oco)
        
        z_alfa_medios = abs(norm.ppf(self.Error_Aceptado/2))
        #print(Uco,O2_co,Oco,Zo,z_alfa_medios)
        
        return Zo < z_alfa_medios
        
        
#FIN DE PRUEBAS DE CORRIDAD ARIBA Y ABAJO


#PRUEBA INDEPENDENCIA (PRUEBA DE CORRIDAD ARIBA Y ABAJO)
class corridas_ariba_abajo_media:
    def __init__(self):
         self.Error_Aceptado = 0.05
         self.data = []
         

    def probar(self, archivo):
        
        # 1.- Primero Obtenemos los Numeros Aleatorios
        with open(archivo, 'r') as file:
            contenido = file.read()
        datos = [float(valor) for valor in contenido.split()]
        #Fin de Lectura
        
        # 2.- Segundo Contamos los numeros
        n = len(datos)
        
        # 3.-Conteno de ceros y unos
        lista =[]
        for i in range(n):
            if( datos[i] < 0.5):
                lista.append(0)
            else:
                lista.append(1)
            
        
        
        Co = 1
        n0 = lista.count(0)
        n1 = lista.count(1)
    
        for i in range(len(lista)-1):
            if( lista[i+1] != lista[i]):
                Co = Co + 1
            else:
                Co = Co
                
        Uco = ((2*n0*n1)/n) + ( 1 / 2 )
        O2co = (2*n0*n1*(2*n0*n1-n))/(n**2*(n-1))
        Zo = (Co - Uco) / math.sqrt(O2co)  
        
                
                
        Z_alpha_medios = abs(norm.ppf(self.Error_Aceptado/2))
        #print(lista,Co,n0,n1,Zo,O2co,Uco,Z_alpha_medios)
     
        return Zo < Z_alpha_medios
        
        
#FIN DE PRUEBAS DE CORRIDAD ARIBA Y ABAJO



class Poker:
    def __init__(self):
        self.Error_Aceptado = 0.05
        self.data = []
        self.valores_categoria = {
            'TD': 0.3024,
            '1P': 0.5040,
            '2P': 0.1080,
            'TP': 0.0090,
            'T': 0.0720,
            'PK': 0.0045,
            'Q': 0.0001
        }
    
    def probar(self, archivo):
        # 1.- Primero Obtenemos los Números Aleatorios
        with open(archivo, 'r') as file:
            contenido = file.read()
        
        # Convertir los datos a flotantes
        datos = [float(valor) for valor in contenido.split()]
        
        # 2.- Contamos los números
        n = len(datos)
        
        # Convertir a cada número en str con 5 dígitos
        digitos_decimales = []
        for num in datos:
            
            # Redondear a 5 decimales
            num_rounded = round(num, 5)
            
            # Convertir a cadena con 5 decimales asegurados
            num_str = f"{num_rounded:.5f}"[2:]  # Eliminar '0.' y mantener 5 dígitos
            # Convertir el número a cadena y quitar el '0.' al inicio
            
            num_str = num_str.zfill(5)  # Rellenar con ceros a la izquierda
            digitos_decimales.append(num_str)  # Convertir a str
            
        #print(digitos_decimales)
            
        # Crear un diccionario para contar las categorías
        categorias = {'TD': 0, '1P': 0, '2P': 0, 'T': 0, 'TP': 0, 'PK': 0, 'Q': 0}

        # Contar la frecuencia de cada dígito y clasificar
        for digito in digitos_decimales:
            frecuencia = {}
            for d in digito:
                if d in frecuencia:
                    frecuencia[d] += 1  # Incrementar el contador
                else:
                    frecuencia[d] = 1  # Inicializar el contador
            
            # Verificar las condiciones para clasificar
            if len(frecuencia) == 5: 
                categorias['TD'] += 1  # Todos los dígitos son diferentes
            elif 3 in frecuencia.values():
                if list(frecuencia.values()).count(2) == 1:
                    categorias['TP'] += 1  # Un par y un trío
                elif list(frecuencia.values()).count(2) == 0:
                    categorias['T'] += 1  # Un trío
            elif list(frecuencia.values()).count(2) == 1 and list(frecuencia.values()).count(3) == 0:
                categorias['1P'] += 1  # Un par
            elif list(frecuencia.values()).count(2) == 2:
                categorias['2P'] += 1  # Dos pares
            elif 4 in frecuencia.values():
                categorias['PK'] += 1  # Un póker
            elif 5 in frecuencia.values():
                categorias['Q'] += 1  # Quintilla
            
        # Imprimir resultados
        #print("Conteo de categorías:")
        conteo_categorias = {}

        for categoria, count in categorias.items():
            conteo_categorias[categoria] = count

        # Crear un DataFrame a partir de los resultados
        df = pd.DataFrame(list(categorias.items()), columns=['Categoría', 'Oi'])
        
        df['Ei'] = df['Categoría'].map(self.valores_categoria) * n
        
        # Calcular ((Ei - Oi) ** 2) / Ei y agregarlo al DataFrame
        df['((Ei - Oi) ** 2) / Ei'] = ((df['Ei'] - df['Oi']) ** 2) / df['Ei']
        
        suma =  sum(df['((Ei - Oi) ** 2) / Ei'])
        #print (suma)
        
        
        #PARA QUE SALGA EL 12.59 SE CAMBIO EN EL 1-0.05 EN EL LIBRO SALE 0.05 NADA MAS
        chi_cuadrada =  abs(chi2.ppf(1 - self.Error_Aceptado,6))
        #print (chi_cuadrada)
        # Imprimir el DataFrame
        #print("\nDataFrame de Conteo de Categorías:")
        #print(df)
        
        if (suma > chi_cuadrada):
            return False #RECHAZA QUE LOS NUMEROS SON INDEPENDIENTES
        else:
            return True  #NO SE PUEDE RECHAZAR
        
        

        
        
        
        
        

            
                 
        
        
        
       
        
        
        
        
        
    







  




    
    
    
    
    
    
    
    
    
    
    
    
    
   