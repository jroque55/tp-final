import math
import random
import time
import numpy as np
import scipy.stats as stats

# CB, D y AL variables de control
CB = 0 
D = 0 
AL = 0

def iniciar_valor(nombre, alias ):
    while True:
        try: 
            valor = float(input(f"{nombre}({alias}): "))
            return valor
        except ValueError:
            print("\nError: Ingrese un valor numérico válido.\n")

CB = iniciar_valor("Cantidad de baños", "CB")
D = iniciar_valor("Dias para proximo mantenimiento", "D")
AL = iniciar_valor("Aceptacion de licitacion", "AL")


# Condiciones Iniciales
BD = CB
T = 0
CMI = 0
D_segundos = D * 24 * 60 * 60
TPM = D_segundos
TPP = 0
SCM = 0
SB = 0
CE = 50000
CSB = 0
BN = 0

# 1 año
TF = 60 * 60 * 24 * 365

HV = 9999999


def proximo_pedido():
    global T
    global TPP
    global CSB
    global BD
    global SB
    global CE

    T = TPP
    TPP = T + obtener_IE()
    CSB = int(obtener_PA() * 2)/50
    if(CSB <= BD):
        if(obtener_AL()):
            BD = BD - CSB
            SB = SB + (CSB*50000) - CE 

    

def proximo_mantenimiento():
    global T
    global TPM
    global D
    global CMI
    global BD
    global CB
    global SCM

    T = TPM
    TPM = T + D_segundos
    CMI = CMI + BD
    BD = CB
    SCM = SCM + CB * 15000

def obtener_IE():
    R = random.uniform(0,1)
    a = -0.0001
    valor = (np.log(-R + 1))/(a)
    return valor

def obtener_PA():
    R = random.uniform(0,1)
    a = -260.31106835432
    b = 853.4952840841792
    valor = stats.gibrat.ppf(R, a, b)
    return valor



def obtener_AL():
    global AL

    R = random.uniform(0,1)
    if(R <= AL):
        return True
    else:
        return False
    

def resultados():
    global BN
    global SB
    global SCM
    global CMI

    print("\n\n### Resultados ###\n\n")

    BN = SB - SCM

    print(f"Beneficio Neto: {BN}")
    print(f"Cantidad de Mantenimientos Innecesarios: {CMI}")
    print(f"Dias para proximo mantenimiento: {D}")
    print(f"Cantidad de baños: {CB}")
    print(f"Aceptacion de licitacion: {AL}")



def realizar_simulacion():
    global T
    global TPM
    global TPP
    global TF

    while True: 
        if TPM <= TPP:
            proximo_mantenimiento()
        else: 
            proximo_pedido()
        
        if T < TF:
            continue
        else:
            break
    
    resultados()




def main():
    print("\n\n### Comenzando simulacion ###\n\n")
    realizar_simulacion()
    print("\nFinalizando simulacion...")

if __name__ == "__main__":
    main()