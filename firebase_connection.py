# firebase_connection.py
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

# Ruta al archivo de configuración de Firebase descargado
cred = credentials.Certificate("imagensCout.json")

# Especifica el ID de tu proyecto de Firebase
project_id = "back-flutter-a83ed"  # Reemplaza "your-project-id" con el ID de tu proyecto

# Inicializar la aplicación de Firebase con el nombre del bucket y el proyecto
initialize_app(cred, options={
    'storageBucket': 'back-flutter-a83ed.appspot.com',
    'projectId': project_id
})

# Obtén una referencia a la colección en Firestore
db_firestore = firestore.client()
