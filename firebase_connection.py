# firebase_connection.py
import firebase_admin
import os
from firebase_admin import credentials, firestore, initialize_app
from dotenv import dotenv_values

# Cargar las variables de entorno desde el archivo .env
env_variables = dotenv_values('.env')

# Verifica que las variables de entorno se hayan cargado correctamente
print("Variables de entorno cargadas:")
print("JSON_FIREBASE:", env_variables.get('JSON_FIREBASE'))
print("PROJECT_ID:", env_variables.get('PROJECT_ID'))
print("BUCKET:", env_variables.get('BUCKET'))

# Ruta al archivo de configuración de Firebase descargado
# Ruta al archivo de configuración de Firebase descargado
firebase_credential_path = os.path.join(os.path.dirname(__file__), env_variables.get('JSON_FIREBASE'))

# Inicializar la aplicación de Firebase con el nombre del bucket y el proyecto
initialize_app(credentials.Certificate(firebase_credential_path), {
    'storageBucket': env_variables.get('BUCKET'),
    'projectId': env_variables.get('PROJECT_ID')
})
# Obtén una referencia a la colección en Firestore
db_firestore = firestore.client()
