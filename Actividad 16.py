class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    def mostrar_info_libros(self):
        print(f"Titulo: {self.titulo} || Autor: {self.autor} || Año de lanzamiento: {self.anio}")
list_books = []
def add_books():
    try:
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio = int(input("Ingrese el año del libro: "))
        book = Libro(titulo, autor, anio)
        list_books.append(book)
        print("\n Se a añadido el libro")
    except ValueError:
        print("El valor debe ser entero")

