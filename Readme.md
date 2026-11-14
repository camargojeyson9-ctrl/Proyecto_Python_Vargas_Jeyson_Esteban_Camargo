1. main.py (La Interfaz y el Menú)
Este archivo se encarga exclusivamente de interactuar con el usuario a través de la terminal (usando print e input).

Funciones principales:

Mostrar el menú de bienvenida y la pantalla de Login. OK

Mostrar el menú principal según el rol (médico o administrativo).

Coordinar el flujo visual: pedir datos por pantalla y llamar a las funciones del archivo de lógica.

2. logica.py (Las Reglas del Negocio)
Aquí concentras todas las operaciones y reglas que pide la clínica, sin tocar la consola ni preocuparte por abrir archivos directamente.

Funciones principales:

Autenticación: Validar si el correo y la contraseña coinciden. OK

Inicialización: Verificar si existe el archivo de usuarios y, si está vacío o no existe, crear automáticamente al usuario Admin con los datos obligatorios. OK

Gestión de Pacientes: Validar y estructurar la información del nuevo paciente. OK

Diagnóstico y Prescripción: Agrupar los síntomas, la patología y la prescripción médica (medicamento, cantidad, dosis, días) y estructurar el diccionario que se convertirá en JSON. OK

Historia Clínica: Buscar por número de identificación y armar el consolidado de consultas anteriores del paciente.

3. database.py (La Persistencia)
Un archivo pequeño dedicado únicamente a la manipulación de los archivos .json.

Funciones principales:

Una función genérica para leer datos de cualquier archivo JSON (devolviendo una lista o diccionario). OK

Una función genérica para guardar o actualizar datos en un archivo JSON. OK

Esto evita que tengas que repetir código de manejo de archivos en el resto de la aplicación.

4. Carpeta /data
Una carpeta simple en el directorio raíz de tu proyecto donde se almacenarán los archivos físicos:

usuarios.json

pacientes.json

prescripciones.json (o el almacenamiento de las consultas)