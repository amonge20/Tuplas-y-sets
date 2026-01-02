# TRABJANDO CON TUPLAS:
# 1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una
# nueva linea.
mi_tupla_1 = ("fruta",45,True)

print("Punto 1")
for tupla in mi_tupla_1:
    print(tupla)

print("")

# 2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla.
# ¿Cuáles son las diferencias?
mi_lista = ["fruta",45,True]
mi_tupla_2 = ("fruta",45,False)

mi_lista[0] = "Pera"
# mi_tupla_2[0] = "Verdura"

print("Punto 2")
print(mi_lista) # En lista si que se puede modificar el cambio de listado
# print(mi_tupla_2) pero en cambio con una tupla no soporta de que la lista se modifique
print("")

# 3. Crea una tupla de enteros y devuelve la suma de los elementos.
tupla_enteros = (1,5,10,15)
tupla_suma = sum(tupla_enteros)

print("Punto 3")
print(tupla_suma)
print("")

# 4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el
# primer caracter de cada string.
tupla_strings = ("Aitor","Monge","Santiago")

primera_letra = [letra[0] for letra in tupla_strings]
print("Punto 4")
print(primera_letra)
print("")

# 5. Crea un script que dada una tupla de números devuelva el producto de todos los
# números pares.
tupla_numeros = (1,2,3,4,5,6,7,8,9,10)

tupla_pares = [l for l in tupla_numeros if l % 2 == 0]
print("Punto 5")
print(tupla_pares)
print("")

# 6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros
# ordeandos en orden descendente.
tupla_desordenada = (7, 2, 9, 1, 5, 10, 3, 8, 6, 4)

# Convertimos la tupla en lista
lista = list(tupla_desordenada)

# Ordenamos la lista de forma descendente
lista.sort(reverse=True)

# Convertimos de nuevo a tupla
tupla_ordenada = tuple(lista)

print("Punto 6")
print(tupla_ordenada)
print("")

# 7. Crea un script que dada una tupla con números enteros repetidos, elimine los
# duplicados. (Puedes usar sets).
tupla_numeros_duplicados = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10)

Tupla_no_Repetida = tuple(set(tupla_numeros_duplicados))
print("Punto 7")
print(Tupla_no_Repetida)
print("")

# 8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el
# numero se encuentra en la tupla y falso en el caso contrario.
Numero = 7

Esta_nTupla = Numero in tupla_numeros
print("Punto 8")
print(Esta_nTupla)
print("")

# 9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.
tupla_sinfusionar1 = (1,2,3,4,5)
tupla_sinfusionar2 = (6,7,8,9,10)

tuplasFusionadas = tuple(tupla_sinfusionar1 + tupla_sinfusionar2)
print("Punto 9")
print("Lista de tuplas sin fusionar:",tupla_sinfusionar1,tupla_sinfusionar2)
print("Lista de tuplas fusionado:",tuplasFusionadas)
print("")

# 10. Crea un script que dada una tupla de números devuelva e máximo y el mínimo.
tuplaMaxima = max(tupla_numeros)
tuplaMinima = min(tupla_numeros)

print("Punto 10")
print("Numero maximo:",tuplaMaxima)
print("Numero minimo:",tuplaMinima)
print("")

# 11. Crea un script que dada una tupla con strings devuelva el string más largo y el más
# corto. (Prueba añadiendo key=len a las funciones max y min).
tuplaLongitudMax = max(tupla_strings, key=len)
tuplaLongitudMin = min(tupla_strings, key=len)

print("Punto 11")
print("Longitud maxima:",tuplaLongitudMax)
print("Longitud minima:",tuplaLongitudMin)
print("")

# 12. Crea un script que dada una tupla devuelva el contenido en orden revertido.
tupla_revertida = tupla_desordenada[::-1]

print("Punto 12")
print("Tupla revertida:",tupla_revertida)
print("")

# 13. Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos
# elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos
# elementos de la tupla interna correspondiente.
suma_de_tuplas = ((1,2),(3,4),(5,6),(7,8),(9,10))

tupla_suma_interna = tuple(a + b for a,b in suma_de_tuplas)

print("Punto 13")
print(tupla_suma_interna)