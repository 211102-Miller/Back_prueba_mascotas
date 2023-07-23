# firebase_connection.py
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

# Ruta al archivo de configuración de Firebase descargado
cred = credentials.Certificate("imagensCout.json")
# Inicializar la aplicación de Firebase con el nombre del bucket
initialize_app(cred, options={
    'storageBucket': 'back-flutter-a83ed.appspot.com'
})

# Obtén una referencia a la colección en Firestore
db_firestore = firestore.client()
