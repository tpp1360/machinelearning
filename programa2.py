"""Ejemplo:
    Pedir dos números enteros al usuario e indicar qué número es mayor que otro o si son iguales
"""

Num1 = int(input("Ingresa el primer numero entero: "))

Num2 = int(input("Ingresa el segundo numero entero: "))


if Num1 > Num2:
    print(" El mayor es "+str(Num1))
elif Num1 == Num2:
    print(" Som Iguales "+str(Num1))
else:
    print(" El mayor es "+str(Num2))    

""" 
 Ejemplo:
    Mostrar tres veces la palabra hola
"""
word1 = "Hola"
word2 = "Mundo"

for i in range(3):
    print(word1)

print(word2)

semana = ["Lunes","Miercoles","Viernes"]

for dia in semana:
    print (dia, end ="/")