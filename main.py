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