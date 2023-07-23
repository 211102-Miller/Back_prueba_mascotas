#from firebase_admin import firestore
from firebase_connection import db_firestore
import uuid

class User:
    @staticmethod
    def register(nombre, email, ciudadEstado, contrasena):
        document_id = str(uuid.uuid4())
        data_firestore = {
            'nombre': nombre,
            'email': email,
            'ciudadEstado': ciudadEstado,
            'contrasena': contrasena,
        }
        db_firestore.collection('register').document(document_id).set(data_firestore)
