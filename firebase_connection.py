# firebase_connection.py
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from dotenv import dotenv_values

# Cargar las variables de entorno desde el archivo .env
env_variables = dotenv_values('venv/.env_todo')

# Ruta al archivo de configuración de Firebase descargado
cred = credentials.Certificate(env_variables.get('JSON_FIREBASE'))


# Inicializar la aplicación de Firebase con el nombre del bucket y el proyecto
initialize_app(cred, options={
    'storageBucket': env_variables.get('BUCKET'),
    'projectId': env_variables.get('PROJECT_ID')
})

# Obtén una referencia a la colección en Firestore
db_firestore = firestore.client()
storage_bucket = firebase_admin.storage.bucket()
