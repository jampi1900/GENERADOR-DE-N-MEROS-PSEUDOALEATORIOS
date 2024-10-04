#Productos Medios
 #Selecciona una semilla X0 con D > 3
 #Selecciona una semilla X1 con D > 3
 #Sea Y(i) = X(i) + X(i+1)
 #D digitos del centro de Y(i)
 #R(i)
 
#pip --version (version)
#python get-pip.py (douwload)
#pip install pandas (instalo pandas)

import pandas as pd


#1111111111111111
class Cuadrados_Medios:
    def __init__(self):
        self.data = []  # Lista para almacenar los datos como diccionarios

    def generar(self, semilla):
        D = len(str(semilla))  # Tamaño de Semilla
        semilla_cuadrada = str(int(semilla) ** 2)  # Al cuadrado y comparamos si es par o impar

        # Asegurarse de que semilla_cuadrada tenga longitud par
        if ((len(semilla_cuadrada) % 2 != 0 and D % 2 == 0) or
            (len(semilla_cuadrada) % 2 == 0 and D % 2 != 0)):
            semilla_cuadrada = '0' + semilla_cuadrada


        while len(semilla_cuadrada) < D:
            semilla_cuadrada = '0' + semilla_cuadrada


        #Obtenemos los del medio
        Long = len(semilla_cuadrada)
        start = (Long - D) // 2
        end = start + D
        new_semilla = semilla_cuadrada[start:end]



        R = ('0.' + str(new_semilla))

        # Guardar los datos en un diccionario
        self.data.append({
            'Xi': semilla,
            'Yi': semilla_cuadrada,
            'Medios': new_semilla,
            'Ri': R
        })

        return R, new_semilla


#22222222222222222
class Multiplicador_Constante:
    def __init__(self, a):
        self.data = []
        self.a = a
    
    def generar(self, semilla):
        D = len(str(semilla)) 
        Y_str = str(self.a * int(semilla))
        
        if ((len(Y_str) % 2 != 0 and D % 2 == 0) or
            (len(Y_str) % 2 == 0 and D % 2 != 0)):
            Y_str = '0' + Y_str
            
        while len(Y_str) < D:
            Y_str = '0' + Y_str
            
            
        
            
        Long = len(Y_str)
        start = (Long - D) // 2
        end = start + D
        new_semilla = str(Y_str[start:end])
        
        R = '0.' + str(new_semilla)  # Resultado como un número entre 0 y 1

        # Guardar los datos en un diccionario
        self.data.append({
            'a': self.a,
            'semilla': semilla,
            'Y(i)': Y_str,
            'New_Semilla': new_semilla,
            'Ri': R
        })

        return R, new_semilla




#33333333333333333
class Productos_Medios:
    def __init__(self):
        self.data = []  # Lista para almacenar los datos como diccionarios

    def generar(self, semilla1, semilla2):
        D = len(str(semilla1))  # Tamaño de Semilla
        Y_str = str(int(semilla1) * int(semilla2))  # Multiplicar las dos semillas
         # Asegurarse de que semilla_cuadrada tenga longitud par
        if ((len(Y_str) % 2 != 0 and D % 2 == 0) or
            (len(Y_str) % 2 == 0 and D % 2 != 0)):
                 Y_str = '0' + Y_str
                 
        while len(Y_str) < D:
            Y_str = '0' + Y_str
            
        # Obtener los dígitos centrales de Y
        Long = len(Y_str)
        start = (Long - D) // 2
        end = start + D
        new_semilla = str(Y_str[start:end])


        R = ('0.' + str(new_semilla))  # Resultado como un número entre 0 y 1
        # Guardar los datos en un diccionario
        self.data.append({
            'X1': semilla1,
            'X2': semilla2,
            'Y(i)': Y_str,
            'Medios': new_semilla,
            'Ri': R
        })

        return R, new_semilla
    
    
    
    
    
#44444444444444  
class congruencial_lineal():
    def __init__(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m
        self.data = [] 

    def generar(self, semilla):
        # Calculamos Xi+1 = (a * Xi + c) % m
        new_semilla = (  ( ((self.a) * int(semilla)) + self.c ) % self.m )
        # Calcular r_{i+1} como Xi+1 / (m-1)
        R = str(float((new_semilla) / (self.m - 1)))
        self.data.append({
            'Semilla': semilla,
            'Nueva Semilla': new_semilla,
            'Ri': R
        })
        return R, new_semilla
    
#555555555555555
class congruencial_multiplicativo:
    def __init__(self, a, m):
        self.a = a
        self.m = m
        self.data = [] 
        
    def generar(self, semilla):
        # Calculamos Xi+1 = (a * Xi) % m
        new_semilla = (self.a * semilla) % self.m
        # Calcular r_{i+1} como Xi+1 / (m-1)
        R = new_semilla / (self.m - 1)
        
        # Guardar los datos generados en una lista de diccionarios
        self.data.append({
            'Semilla': semilla,
            'Nueva Semilla': new_semilla,
            'Ri': R
        })
        return R, new_semilla

#666666666666666


class congruencial_aditivo:
    def __init__(self, m):
        self.m = m
        self.data = [] 
        
    def generar(self, semilla):
        D = len(semilla)
        # Calculamos nueva semilla
        new_semilla = (semilla[-1] + semilla[-D]) % self.m
        # Calcular r_{i+1} como Xi+1 / (m-1)
        R = new_semilla / (self.m - 1)
        
        # Guardar los datos
        self.data.append({
            'Semilla': semilla.copy(),  # Guardar copia de la semilla actual
            'Nueva Semilla': new_semilla,
            'Ri': R
        })
        
        return R, new_semilla

#777777777777777
class congruencial_cuadratico:
    def __init__(self, a, b, c, m):
        self.a = a
        self.b = b
        self.c = c
        self.m = m
        self.data = [] 
        
    def generar(self, semilla):
        # Calculamos Xi+1 = (a * Xi^2 + b * Xi + c) % m
        new_semilla = (self.a * (semilla ** 2) + self.b * semilla + self.c) % self.m
        # Calcular r_{i+1} como Xi+1 / (m-1)
        R = new_semilla / (self.m - 1)
        
        # Guardar los datos
        self.data.append({
            'Semilla': semilla,
            'Nueva Semilla': new_semilla,
            'Ri': R
        })
       
        return R, new_semilla

    




    





