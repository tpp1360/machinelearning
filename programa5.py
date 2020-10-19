
""" Ejercicio:
    1) Solicitar dos numeros en consola y mostrar la suma.
"""

def sumar(a,b):
    s=a+b
    return s

x = float(input(" Ingresa el primer numero: "))
y = float(input(" Imgresa el segundo numero: "))


print(" La suma: "+ str(sumar(x,y)))