import hashlib

#funcion para cifrar la contraseña introducida para posteriormente compararla con la del fichero de los usuarios
def cifrar(contraseña):
    return hashlib.md5(contraseña.encode()).hexdigest()

#funcion para guardar los usuarios en forma de diccionario haciendo que la contraseña 
#cifrada sea el valor de la clave que es el nombre del usuario
def leerUsuarios():
    usuarios = {}
    try:
        archivoUsuarios = open("Usuaris.txt", "r")
        lineas = archivoUsuarios.readlines()
        archivoUsuarios.close()
        for linea in lineas:
            usuario, contraseña = linea.strip().split("|")
            usuarios[usuario] = contraseña
    except FileNotFoundError:
        print("error: no se encontro el archivo de usuarios.")
    return usuarios

#funcion para el inicio de sesion con un numero de intentos espeficados al principio del programa y se llama
#la funcion de cifrar para cifrar la contraseña que se va a introducir y se comparar con el valor de las claves
def inicioSesion():
    intentos = 0
    usuarios = leerUsuarios()
    while intentos < 3:
        print("pon tus credenciales o (adios) para salir, tienes 3 intentos")
        usuario = input("usuario: ")
        if usuario.lower() == "adios":
            print("¡adeu guap@!")
            return None
        contraseña = cifrar(input("contraseña: "))
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("inicio de sesion exitoso!")
            return usuario
        else:
            print("el usuario o contraseña son incorrectos.")
            intentos += 1
            print(f"intento numero {intentos}\n")

    print("has fallado ya tres veces, piensa tus credenciales y vuelve ;).")
    return None

#funcion para mostar un libro en concreto recorriendo el fichero linea por linea comprovando si el titulo 
#introducido se encuentra en la posicion 0 de cada linea(libro)
def mostrarLibro(titulo):
    if not titulo.strip():
        print("pon el título del libro que deseas mostrar porfavor.")
        return

    try:
        archivoLibros = open("Llibres.txt", "r")
        for linea in archivoLibros:
            atributos = linea.strip().split("|")
            if titulo in atributos[0]:
                print(f"titulo: {atributos[0]} - autor: {atributos[1]} - año: {atributos[2]} - genero: {atributos[3]} - isbn: {atributos[4]}")
                archivoLibros.close()
                return
        print("no hemos encontrado el libro.")
        archivoLibros.close()
    except FileNotFoundError:
        print("error: no se encontro el archivo de libros.")

#funcion para agregar un libro y añadiendolo al final del fichero, primero se verifica de que el libro no exista y luego 
#se añade con el atributo (a) para que sea al final del fichero
def agregarLibro():
    titulo = input("titulo del libro: ")
    autor = input("autor/a: ")
    año = input("año de publicacion: ")
    genero = input("genero: ")
    isbn = input("isbn: ")

    if not titulo.strip() or not autor.strip() or not año.strip() or not genero.strip() or not isbn.strip():
        print("error: todos los campos son obligatorios si quieres agregar un libro.")
        return

    try:
        archivoLibros = open("Llibres.txt", "r")
        lineas = archivoLibros.readlines()
        archivoLibros.close()

        for linea in lineas:
            if titulo in linea:
                print("este libro ya existe.")
                archivoLibros.close()
                return

        archivoLibros = open("Llibres.txt", "a")
        archivoLibros.write(f"{titulo}|{autor}|{año}|{genero}|{isbn}\n")
        print("libro agregado con exito.")
        archivoLibros.close()
    except FileNotFoundError:
        print("error: no se encontro el archivo de libros.")

#funcion para eliminar un libro, se pide el ttulo del libro que se desea eliminar y posteriormente se vacia el fichero y se
#va escibiendo de nuevo linea por linea y si el titulo se encuentra an alguna lina la condicon booleana se vuelve True y no escribe
#ese libro para que asi el fichero final este sin el libro que queriamos eliminar
def eliminarLibro(titulo):
    if not titulo.strip():
        print("pon el título del libro que deseas eliminar porfavor.")
        return

    try:
        archivoLectura = open("Llibres.txt", "r")
        lineas = archivoLectura.readlines()
        archivoLectura.close()

        encontrado = False
        archivoEscritura = open("Llibres.txt", "w")
        for linea in lineas:
            if titulo not in linea:
                archivoEscritura.write(linea)
            else:
                encontrado = True
        archivoEscritura.close()

        if encontrado:
            print("libro eliminado correctamente.")
        else:
            print("el libro no se encontro.")
    except FileNotFoundError:
        print("error: no se encontro el archivo de libros.")

#funcion para editar algun libro, se pide un titulo de alguna libro en el principio del programa. Se leen todas las lineas(libros) del 
#fichero, se abre el fichero para la sobreescriptura i la linea que contenga el titulo proporcionado ira preguntado si se quiero cambiar 
#algun atributo del libro o dejarlo igual
def editarLibro(titulo):
    if not titulo.strip():
        print("pon el título del libro que deseas editar porfavor.")
        return

    try:
        archivoLectura = open("Llibres.txt", "r")
        lineas = archivoLectura.readlines()
        archivoLectura.close()

        archivoEscritura = open("Llibres.txt", "w")
        for linea in lineas:
            atributos = linea.strip().split("|")
            if titulo in atributos[0]:
                print("editando el libro:", atributos[0])
                nuevoTitulo = input(f"pon el nuevo titulo del libro (actual: {atributos[0]}): ") or atributos[0]
                nuevoAutor = input(f"pon el nuevo autor/a (actual: {atributos[1]}): ") or atributos[1]
                nuevoAño = input(f"pon el nuevo año de publicacion (actual: {atributos[2]}): ") or atributos[2]
                nuevoGenero = input(f"pon el nuevo genero (actual: {atributos[3]}): ") or atributos[3]
                nuevoIsbn = input(f"pon el nuevo isbn (actual: {atributos[4]}): ") or atributos[4]

                nuevaLinea = f"{nuevoTitulo}|{nuevoAutor}|{nuevoAño}|{nuevoGenero}|{nuevoIsbn}\n"
                archivoEscritura.write(nuevaLinea)
                print("libro editado con exito.")
            else:
                archivoEscritura.write(linea)
        archivoEscritura.close()
    except FileNotFoundError:
        print("error: no se encontro el archivo de libros.")