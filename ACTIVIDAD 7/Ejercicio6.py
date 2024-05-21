#Se importan los modulos necesarios
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageFilter

#Funcionalidades agregadas: Verificar los hilos creados
import threading
import time


#Se define la funcion para aplicar el filtro
def aplicar_filtro(imagen_path):
    print(f"Hilo {threading.current_thread().name} iniciado")
    
    #Tomando el tiempo por cada hilo
    t_i=time.time()

    img = Image.open(imagen_path)
    img = img.filter(ImageFilter.GaussianBlur(5))
    img.save(f"{imagen_path}_blurred.jpg")
    print(f"Filtro aplicado a {imagen_path}")
    
    t_f=time.time()

    print("Tiempo tomado por un hilo", t_f-t_i)

    return t_f-t_i

#Crear un pool de threads y distribuir las tareas
imagenes = ["imagen1.jpg", "imagen2.jpg", "imagen3.jpg"]

with ThreadPoolExecutor(max_workers=3) as executor:
     tiempo=executor.map(aplicar_filtro, imagenes)
     print(sum(tiempo))

