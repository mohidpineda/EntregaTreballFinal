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