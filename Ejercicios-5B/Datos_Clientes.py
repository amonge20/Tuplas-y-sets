# Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene
# el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La
# segunda base de datos contiene el nombre del cliente, la dirección y el historial de
# pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y
# devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en
# ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre.
# Pista: Tus datos de entrada podrían ser así —>
# base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria",
# "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", “555-9012")]
# base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]),
# ("Luis", "Calle 789", ["Libro4"])]

# Base de datos 1
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria","maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]

# Base de datos 2
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]

# Nueva lista en tupla
clientes = []

# Comparamos el nombre de cada usuario en las 2 bases de datos creadas
for cliente1 in base_datos1:
    nombre = cliente1[0]
    for cliente2 in base_datos2:
        nombre1 = cliente2[0]
        # Si hay alguna en que coincida, se añadira en la nueva lista
        if nombre == nombre1:
            clientes.append((cliente1, cliente2))

print(clientes)