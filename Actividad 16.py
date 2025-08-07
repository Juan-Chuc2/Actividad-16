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
            print(f"{j}. ", end="")
            book.mostrar_info()
            j += 1

def delete_book():
    search_book = input("Ingrese el titulo del libro que desea buscar: ")
    found = False
    for book in list_books:
        if book.titulo.lower() == search_book.lower():
            list_books.remove(book)
            print(f"\n El titulo {search_book} se ha eliminado correctamente")
            found = True
            break
        if not found:
            print(f"\n El estudiante {search_book} no se encontro")

while True:
    print("---MENU---")
    print("1. Agregar libro ")
    print("2. Mostrar libros")
    print("3. Eliminar libro")
    print("4. Salir")
    try:
        option = int(input("Escoja una opcion "))
        match option:
            case 1:
                add_books()
            case 2:
                show_book()
            case 3:
                delete_book()
            case 4:
                print("Fin del programa")
                break
            case _:
                print("Erro ingrese unu entero")
    except ValueError:
        print("Ingrese un entero")