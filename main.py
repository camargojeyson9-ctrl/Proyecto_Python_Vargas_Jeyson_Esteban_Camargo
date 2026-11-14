from logica import(
    iniciar_admin,
    validar_login,
    registrar_usuario,
    registrar_paciente,
    diagnostico_paciente,
    historia_clinica,
)

def main():

    iniciar_admin()

# Bienvenida a el programa e llamamos la funcion iniciar admin para tener el primer usuario registrado.
    while True:
        print("\n                   ---BIENVENIDO A ACME CLINIC---                              \n")
        print("A continuacion ingresa tu correo electronico y contraseña para entrar al programa\n")

    # Flujo inicio de sesion.

        correo_ingreso = input("Si deseas cerrar el programa escribe (Salir) si deseas ingresar escribe tu correo electronico: ").strip()
        if correo_ingreso.lower() == "salir": # Lo blinda en caso de que el usuario escriba Salir
            print("\nSaliendo del programa, nos vemos en una proxima ocasion.")
            break

        contraseña_ingreso = input("Ingresa tu contraseña: ").strip()

        usuario_actual = validar_login(correo_ingreso,contraseña_ingreso)

        if usuario_actual:
            print("Bienvenido al sistema de ACME CLINIC")
            print(f"Su rol en el sistema:{usuario_actual['rol'].upper()}") #upper convierte las letras en Mayuscula

            rol = usuario_actual["rol"].lower()

            if rol == "admin":
                menu_admin(usuario_actual)

            elif rol == "medico":
                menu_medico(usuario_actual)

            else:
                print("Tu sesion no cuenta con permisos para interactuar en el programa.")
                print("\nCesion cerrada, vuelve a iniciar sesion o escribe Salir para cerrar el programa")

        else:
            print("Credenciales incorrectas, vuelve a intentarlo nuevamente\n")


# Creacion de funcion para el menu de usuarios con Rol administrador.
def menu_admin(usuario):

    # Bucle para repetir el menu hasta cerrarlo.
    while True:

        print("\n--- MENU ADMINISTRADOR ---\n")
        print(f"Bienvenido, {usuario['nombres']} {usuario['apellidos']}")
        print("1.Registrar nuevo usuario (Medico o Admin)")
        print("2.Registrar nuevo paciente")
        print("3.Salir del programa\n")
        
        opcion_admin = input("\nIngresa la opcion del menu que deseas realizar: ").strip()

        # creacion de usuario.
        if opcion_admin == "1":
            print("\n---REGISTRO NUEVO USUARIO---")
            print("\nA continuacion vamos a registrar un nuevo usuario")

            identificacion = input("Ingresa el numero de indentificacion: ").strip()
            nombres = input("Ingresa los nombres del usuario: ").strip()
            apellidos = input("Ingresa los apellidos del usuario: ").strip()
            telefono = input("Ingresa el numero de telefono: ").strip()
            correo = input("Ingresa el correo electronico: ").strip()
            contraseña = input("Ingresa la contraseña con la cual el usuario iniciara cesion: ").strip()
            direccion = input("Ingresa la direccion de residencia: ").strip()
            rol = input("Ingresa el rol del usuario: ").strip().lower()

            resultado, mensaje = registrar_usuario(identificacion,nombres,apellidos,telefono,correo,contraseña,direccion,rol)
            print(f"{mensaje}")


        # creacion de paciente.
        elif opcion_admin == "2":
            print("\n---REGISTRO NUEVO PACIENTE---")
            print("\nA continuacion vamos a registrar un nuevo paciente")

            identificacion_p = input("Ingresa el numero de indentificacion: ").strip()
            nombres_p = input("Ingresa los nombres del usuario: ").strip()
            apellidos_p = input("Ingresa los apellidos del usuario: ").strip()
            telefono_p = input("Ingresa el numero de telefono: ").strip()
            correo_p = input("Ingresa el correo electronico: ").strip()
            direccion_p = input("Ingresa la direccion de residencia: ").strip()
            genero_p = input("Ingresa el genero del paciente: ").strip()
            estado_civil = input("Ingrese el estado civil del paciente: ").strip()

            resultado, mensaje = registrar_paciente(identificacion_p,nombres_p,apellidos_p,telefono_p,correo_p,direccion_p,genero_p,estado_civil)
            print(f"{mensaje}")

        elif opcion_admin == "3":
            print("\nElegiste la opcion de salir del programa")
            print("Nos vemos en una proxima ocasion\n")
            break

        else:
            print("\nError, has elegido una opcion invalida, te devolveremos al menu para que lo vuelvas a intentar")

# creacion de 
def menu_medico(usuario):

    # Bucle para repetir el menu hasta cerrarlo.
    while True:

        print("\n--- MENU MEDICO ---")
        print("1.Registrar nuevo diagnostico y preescripcion medica de un paciente")
        print("2.Consultar historial clinico del paciente")
        print("3.Salir del programa\n")

        opcion_medico = input("\nIngresa la opcion del menu que deseas realizar: ").strip()

        if opcion_medico == "1":
            print("\n---NUEVO DIAGNOSTICO---")
            print("\nA continuacion vamos a registrar el diagnostico del paciente")

            identificacion_paciente = input("Ingresa la identificacion del paciente: ").strip()
            nombre_paciente = input("Ingresa el nombre del paciente: ").strip()
            sintomas = input("Ingresa los sintomas del paciente: ").strip()
            diagnostico = input("Ingresa el diagnostico del paciente: ").strip()

            print("\n--- Preescripcion medica ---\n")
            medicamento = input("Ingresa el medicamento a recetar al paciente: ").strip()
            cantidad = input("Ingresa la cantidad de medicamento a ingerir el paciente: ").strip()
            dosis = input("Ingresa la cantidad de dosis que debe tomar el paciente: ").strip()
            tiempo_aplicacion = input("Ingresa el tiempo de aplicacion del medicamento: ").strip()
            fecha_consulta = input("Ingresa la fecha de la consulta: ").strip()
            nombre_medico = f"{usuario['nombres']} {usuario['apellidos']}".strip()

            resultado, mensaje = diagnostico_paciente(identificacion_paciente,nombre_paciente,sintomas,diagnostico,medicamento,cantidad,dosis,tiempo_aplicacion,fecha_consulta,nombre_medico)
            print(f"{mensaje}")

        elif opcion_medico == "2":
            print("\n---HISTORIAL CLINICO DEL PACIENTE---")
            print("\nA continuacion veremos el historial del paciente")
            identificacion_paciente = input("Ingresa la documentacion del paciente: ").strip()
            exito, historial = historia_clinica(identificacion_paciente)

            if exito:
                print("\n--- HISTORIAL DEL PACIENTE ---")

                for i,consulta in enumerate(historial,1):
                    print(f"\nConsulta{i}")
                    print(f"Identificacion:{consulta.get('identificacion_paciente')}")
                    print(f"Nombre paciente:{consulta.get('nombre_paciente')}")
                    print(f"Fecha:{consulta.get('fecha_consulta')}")
                    print(f"Medico:{consulta.get('medico')}")
                    print(f"Sintomas:{consulta.get('sintomas')}")
                    print(f"Diagnostico:{consulta.get('diagnostico')}")

                    print("\nPreescripcion Medica\n")
                    preescripcion = consulta.get('preescripcion',{})
                    print(f"Medicamento:{preescripcion.get('medicamento')}")
                    print(f"Cantidad:{preescripcion.get('cantidad')}")
                    print(f"Dosis:{preescripcion.get('dosis')}")
                    print(f"Tiempo aplicacion:{preescripcion.get('tiempo_aplicacion')}")
                    print("-----------------------------------------------------------")

            else:
                print("El usuario no existe o no tiene registros")


        elif opcion_medico == "3":
            print("\nElegiste la opcion de salir del programa")
            print("Nos vemos en una proxima ocasion\n")
            break

        else:
            print("\nElegiste una opcion invalida, vuelve a intentarlo nuevamente\n")

if __name__=="__main__":
    main()