#Importa el modulo necesario
import multiprocessing
import math

import sys
sys.set_int_max_str_digits(0)

import os

import time

#Define la funcion que calcula el factorial
def calcular_factorial(numero):
    print(f"Proceso {os.getpid()} iniciado")
    resultado=math.factorial(numero)
    #print(f"El factorial de {numero} es {resultado}")
    return resultado

#Crea una lista de numeros
numeros=[1000 + x for x in range(5)]

#Distribuye la tarea entre multiples procesos:
if __name__=="__main__":
    t_i=time.time()
    with multiprocessing.Pool(5) as pool:
        resultados=pool.map(calcular_factorial,numeros)
    print(resultados)
    t_f=time.time()
    print("Tiempo total:",t_f-t_i)

