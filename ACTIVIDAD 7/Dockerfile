#Colocamos la imagen base
FROM ubuntu
#Actualizamos el sistema e instalamos python 
RUN apt-get update && apt-get install -y python3
#Ya que fue instalado python, copiamos el archivo .py a una carpeta a la imagen ubuntu instalada
#Primero, asignamos que el directorio home sea el directorio de trabajo
WORKDIR /home

#Ahora, copiamos el archivo .py al directorio actual (en este caso home)
COPY Ejercicio6.py . 

#Finalmente, con el comando cmd ejecutamos el programa
CMD python3 Ejercicio6.py
