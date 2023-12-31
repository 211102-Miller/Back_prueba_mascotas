from firebase_admin import credentials, firestore, storage
import uuid
from firebase_connection import db_firestore
from dotenv import dotenv_values

# Cargar las variables de entorno desde el archivo .env
env_variables = dotenv_values('.env')


class FormAdoptedModel:
    def save_form_data(self, nombre, raza, image, horario, ubicacion):
        filename = image.filename
        document_id = str(uuid.uuid4())
        bucket = storage.bucket(env_variables.get('BUCKET'))
        blob = bucket.blob(f'formAdopted/{filename}')
        blob.content_type = 'image/jpeg'
        blob.upload_from_file(image)
        data_firestore = {
            'nombre': nombre,
            'raza': raza,
            'image': filename,
            'horario': horario,
            'ubicacion': ubicacion,
        }
        db_firestore.collection('FormAdopted').document(document_id).set(data_firestore)
        return document_id
