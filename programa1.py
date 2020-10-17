import constantes

#print(DB_NAME)

mensaje = "Bienvenido a Python 3.8!"
print(mensaje)

message = 'hello world!'
print(message)

nombre =  input("Ingresa tu nombre: ")
print("Bienvenido hijo del rock and roll ," + nombre)

z1 = 6 + 7j
z2 = 8 - 2j

print(z1+z2)

numero =  input(" Ingresa un numero : ")

print(" Ingresaste "+ str(float(numero)))

# Listas

juana = ["Juana Albites", 23, 56.67, 1.60]

print("El peso de "+juana[0]+" es "+str(juana[2]))

# tuplas

office = ("Word","Excel","Power Point")

print(office[1])

# Diccionario

persona = {
   'nombre': "Juana Albites",
   'edad': 23,
   'peso': 56.67,
   'talla': 1.60      
}

print(persona['edad'])

print(persona.keys())

""" Ejercicio:
    1) Solicitar dos numeros en consola y mostrar la suma.

    
"""