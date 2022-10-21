#Este código pide elementos usando input y los almacena en una lista

#Se declara una lista vacía
elementos = []

#Se declara una variable tipo string vacía
cadena = ""

#Se declara el bucle
print("Inserte elementos a la lista. Para terminar el proceso escriba exit")
while True:
    cadena = input("Inserte elemento: ")
    if cadena == "exit":
        break
    else:
        elementos.append(cadena)

print(elementos)