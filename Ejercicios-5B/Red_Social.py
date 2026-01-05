# Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
# Crea un programa que tome una base de datos de una red social como una lista de
# tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
# nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
# diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
# tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.
# Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro",
# "Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan”])]
# Pista 2: Para eliminar duplicidades puedes usar sets 

# Base de datos de los usuarios junto con las listas de amigos
red_social = [("Juan", ["Maria", "Pedro","Luis"]), ("Maria", ["Juan", "Pedro","Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# Eliminanos las cuentas duplicadas segun la solitud de amistad de cada usuario
red_social_unica = set((usuario, tuple(set(amigos))) for usuario, amigos in red_social)

# Contamos el numero real de amigos por usuario
numerosUsuarios = 0

# Creamos un bucle para contar el numero real y la longitud de amigos
for usuario, amigos in red_social_unica:
    numerosUsuarios += len(amigos)
    print(f"{usuario} tiene {len(amigos)} amigo/s")

# Buscamos al usuario con más amigos
Usuario_mas_amigos = max(red_social_unica, key=lambda x: len(x[1]))

print(f"El usuario con más amigos es {Usuario_mas_amigos[0]} con {len(Usuario_mas_amigos[1])} amigos")