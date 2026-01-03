# TRABAJANDO CON SETS:
# 14.Crea un set y elimina uno de sus elementos.
lista_set1 = {"Hola",45,False}

lista_set1.remove("Hola")

print("Punto 14")
print(lista_set1)
print("")

# 15.Crea un set vacío.
lista_set1 = set()
print("Punto 15")
print(lista_set1)
print("")

# 16.Crea dos sets y encuentra su union, su intersección y su diferencia.
# Variables de los sets
set1 = {1,2,3}
set2 = {3,4,5,6}

print("Punto 16")
print("Por su union:",set1.union(set2))
print("Por su intersección comun:",set1.intersection(set2))
print("Por su diferencia:",set1.difference(set2))
print("")

# 17.Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos
# comunes de ambos.
set_comun1 = {1,2,3,4}
set_comun2 = {2,3,4,5}

set_comunJunto = set_comun1.intersection(set_comun2)

print("Punto 17")
print("Numeros comunes:",set_comunJunto)
print("")

# 18.Crea un script que dado un set con números devuelva el numero máximo y mínimo.
set_maxim = {4,6,7,1,10,5,2,8,3,9}

print("Punto 18")
print("Numero maximo:",max(set_maxim))
print("Numero minimo:",min(set_maxim))
print("")

# 19.Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de
# cada uno de los sets.
sets_duplicado1 = {1,1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5}
sets_duplicado2 = {6,6,6,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10}

sets_unicos = sets_duplicado1.union(sets_duplicado2)
print("Punto 19")
print("Sets unicos:",sets_unicos)
print("")

# 20.Crea un set con colores y comprueba si cierto color se encuentra en el set.
colores = {"azul","rojo","verde","amarillo","naranja","rosa"}

print("Punto 20")
print("rojo" in colores) # Verdadero
print("Verde_Oscuro" in colores) # Falso 
print("")

# 21.Crea un script que dados dos sets cree un nuevo set con los elementos que están en
# el primer set pero no en el segundo.
setDiferente1 = {1,2,3,4}
setDiferente2 = {2,3,4,5}

diferenciaSets = setDiferente1 - setDiferente2
print("Punto 21")
print(diferenciaSets)
print("")

# 22.Crea un script que dado un set de enteros devuelva el producto de todos los números
# dentro del set.
bucleNumeros_set = {2,3,4}

producto = 1

for n in bucleNumeros_set:
    producto *= n

print("Resultado del producto:",producto)