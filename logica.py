from database import leer_datos

# Autenticación: Validar si el correo y la contraseña coinciden.
def validar_login(correo_ingresado, contraseña_ingresada):
    usuarios = leer_datos("usuarios.json")

    for usuario in usuarios:
        if usuario.get("correo")==correo_ingresado and usuario.get("contraseña")==contraseña_ingresada:
            return usuario

    
    return None

# Inicialización: Verificar si existe el archivo de usuarios y, si está vacío o no existe, crear automáticamente al usuario Admin con los datos obligatorios.
from database import leer_datos,guardar_datos

def iniciar_admin():
    usuarios = leer_datos("usuarios.json")

    if not usuarios:
        admin={
        "identificacion": "0000",
        "nombres":"Admin",
        "apellidos": "Administrador",
        "telefono": "555000111",
        "correo": "admin@acmeclinic.com",
        "direccion": "Cl 185 #26-85",
        "contraseña":"admin123",
        "rol":"admin",
    }

        usuarios.append(admin)

        guardar_datos("usuarios.json",usuarios)

# Gestión de usuarios: Validar y estructurar la información del nuevo usuario.
from database import leer_datos,guardar_datos

def registrar_usuario(identificacion,nombres,apellidos,telefono,correo,contraseña,direccion,rol):
    usuarios = leer_datos("usuarios.json")

    for usuario in usuarios:
        if usuario.get("identificacion") == identificacion or usuario.get("correo") == correo:
            return False, "Usuario ya se encuentra registrado"

    nuevo_usuario = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo, # Datos para el login
        "contraseña":contraseña, # Datos para el login
        "direccion": direccion,
        "rol":rol,
    }

    usuarios.append(nuevo_usuario)
    guardar_datos("usuarios.json",usuarios)
    return True, "Nuevo usuario registrado"

# Gestión de pacientes: Validar y estructurar la información del nuevo paciente.

from database import leer_datos,guardar_datos

def registrar_paciente(identificacion,nombres,apellidos,telefono,correo,direccion,genero,estado_civil):
    pacientes = leer_datos("pacientes.json")

    for paciente in pacientes:
        if paciente.get("identificacion") == identificacion or paciente.get("correo") == correo:
            return False, "El paciente ya se encuentra registrado." 

    nuevo_paciente = {
        "identificacion" : identificacion,
        "nombres": nombres,
        "apellidos" : apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "genero": genero,
        "estado civil": estado_civil,
    }

    pacientes.append(nuevo_paciente)
    guardar_datos("pacientes.json",pacientes)
    return True, "\nEl paciente se ha guardado con exito"

# Diagnostico pacientes: Validar si el paciente existe, registro de sintomas, diagnostico, preescripcion medica (Medicamento,Cantidad,Dosis, Tiempo de aplicacion), Datos (Fecha,Paciente,Medico)

from database import leer_datos,guardar_datos

def diagnostico_paciente(identificacion,sintomas,diagnostico,medicamento,cantidad,dosis,tiempo_aplicacion,fecha,nombre_paciente,medico):
    pacientes = leer_datos("pacientes.json")

    for paciente in pacientes:
        if paciente.get("identificacion") == identificacion:
            print("El paciente se encuentra registrado, se puede proceder con la consulta.")
            
            diagnosticos = leer_datos("diagnosticos.json")

            nuevo_diagnostico = {
                "identificacion_paciente": identificacion,
                "nombre_paciente": nombre_paciente,
                "sintomas" : sintomas,
                "diagnostico": diagnostico,
                "preescripcion":{
                    "medicamento": medicamento,
                    "cantidad": cantidad,
                    "dosis": dosis,
                    "tiempo_aplicacion": tiempo_aplicacion,
                },
                "fecha_consulta": fecha,
                "medico": medico,
            }

            diagnosticos.append(nuevo_diagnostico)
            guardar_datos("diagnosticos.json",diagnosticos)
            return True, "\nDiagnostico guardado con exito"
        
    return False, "Error el usuario no se encuentra registrado, registralo para poder acceder al meni de Diagnostico"

from database import leer_datos,guardar_datos

def historia_clinica(identificacion):
    diagnosticos = leer_datos("diagnosticos.json")

    historial = []

    for diagnostico in diagnosticos:
        if diagnostico.get("identificacion_paciente") == identificacion:

            historial.append(diagnostico)

    if historial:
        return True, historial

    else:
        return False, "El paciente aun no tiene diagnosticos registrados"
