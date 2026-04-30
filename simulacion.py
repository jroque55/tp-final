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
            CB = int(input("{nombre}({alias}): "))
            break
        except ValueError:
            print("\nError: Solo se permiten numeros enteros.\n")

iniciar_valor("Cantidad de baños", "CB")
iniciar_valor("Dias para proximo mantenimiento", "D")
iniciar_valor("Aceptacion de licitacion", "AL")


# Condiciones Iniciales
BD = CB
T = 0
CMI = 0
TPM = D
TPP = 0
SCM = 0
SB = 0
CE = 50000
D = 0

BN = 0

# 1 MES
TF = 60 * 60 * 24 * 30

HV = 9999999


def TPP():
    global T
    global TPP
    global CSB
    global BD
    global SB
    global CE

    T = TPP
    TPP = T + obtener_IE()
    CSB = (obtener_PA * 2)/50
    if(CSB <= BD):
        if(obtener_AL()):
            BD = BD - CSB
            SB = SB + (CSB*50000) - CE 

    

def TPM():
    global T
    global TPM
    global D
    global CMI
    global BD
    global CB
    global SCM

    T = TPM
    TPM = T + D
    CMI = CMI - BD
    BD = CB
    SCM = SCM + CB * 15000

def obtener_IE():
    R = random.betavariate(0,1)
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
    print(f"Costo Mantenimiento Innecesario: {CMI}")
    print(f"Dias para proximo mantenimiento: {D}")
    print(f"Cantidad de baños: {CB}")
    print(f"Aceptacion de licitacion: {AL}")



def realizar_simulacion():
    global T
    global TPM
    global TPP
    global TF

    while True: 
        if TPP <= TPM:
            TPM()
        else: 
            TPP()
        
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