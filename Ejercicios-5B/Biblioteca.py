# Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
# de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
# libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
# libro y el apellido del autor.
# Pista: Tus datos de entrada podrían ser así —> lista_libros = [(‘El aleph', ‘Jorge Luis
# Borges'), ('Cien años de soledad', ‘Garbriel Garcia Márquez'), ('La ciudad y los perros',
# ‘Mario Vargas Llosa')]

# Variable de la lista de libros en tupla
lista_libros = [
    ('El aleph', 'Jorge Luis Borges'),
    ('Cien años de soledad', 'Gabriel García Márquez'),
    ('La ciudad y los perros', 'Mario Vargas Llosa')
]

# creamos un bucle para crear una nueva lista
nueva_lista = [(libro, autor.split()[-1]) for libro, autor in lista_libros]

print(nueva_lista)
