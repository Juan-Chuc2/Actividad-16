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

def show_book():
    if not list_books:
        print("No se ha añadido ningun libro ")
    else:
        print("\n Lista de libros")
        j = 1
        for book in list_books:
            print(f"{i}. ", end="")
            book.mostrar_info()
            j += 1