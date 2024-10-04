
import numpy as np

class medias:
    def __init__(self, z=1.96):
        self.z = z

    def probar(self, archivo):
        # Leer el archivo manualmente
        with open(archivo, 'r') as file:
            contenido = file.read()
        
        # Dividir el contenido por espacios y convertir a números flotantes
        datos = [float(valor) for valor in contenido.split()]
        n = len(datos)  # Número de datos
        
        # Calcular la media y la varianza
        media = np.mean(datos)
        
        varianza = np.var(datos)
  
        # Calcular el intervalo de confianza
        intervalo = self.z * (1 / np.sqrt(12 * n))
        limite_inferior = (1 / 2) - intervalo
        limite_superior = (1 / 2) + intervalo
        
        print(f"Media : {media}")
        print(f"Limite inferior: {limite_inferior}")
        print(f"Limite superior: {limite_superior}")
        
        # Retornar si la media está dentro del intervalo
        return limite_inferior <= media <= limite_superior