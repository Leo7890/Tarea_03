#encoding UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Programa que pregunta que tipos de boletos quiere el usuario y da el precio total

def calcularPrecioA(numAsientosA):
    precioA = numAsientosA * 400
    return precioA

def calcularPrecioB (numAsientosB):
    precioB = numAsientosB * 250
    return precioB

def calcularPrecioC (numAsientosC):
    precioC = numAsientosC * 135
    return precioC

def main():
    numAsientosA = int(input("Número de boletos clase A: "))
    numAsientosB = int(input("Número de boletos clase B: "))
    numAsientosC = int(input("Número de boletos clase C: "))
    costoTotal = calcularPrecioA(numAsientosA) + calcularPrecioB(numAsientosB) + calcularPrecioC(numAsientosC)
    print("El costo total es: $%.2f" %(costoTotal))

main()
