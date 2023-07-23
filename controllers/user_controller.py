# controllers/user_controller.py
from models.user_models import User
from firebase_connection import db_firestore
from flask import request, jsonify
from utils.jwt_utils import generate_token, verify_token
import jwt
from google.cloud import firestore


def register():
    nombre = request.form['nombre']
    email = request.form['email']
    ciudadEstado = request.form['ciuadadEstado']
    contrasena = request.form['contrasena']

    User.register(nombre, email, ciudadEstado, contrasena)

    return 'Registro de usuario exitoso'

#login
def login():
    email = request.args.get('email')
    contrasena = request.args.get('contrasena')

    # Verificar las credenciales en Firestore
    users_ref = db_firestore.collection('register')
    # Firestore reference
    ddb = firestore.Client()
    users_ref = ddb.collection('users')
    query = users_ref.where('email', '==', email).where('contrasena', '==', contrasena).limit(1)

    results = query.get()

    if len(results) > 0:
        user_data = results[0].to_dict()
        user_id = results[0].id
    
    # Generar el token JWT
        token = generate_token(user_id)

        return jsonify({'message': 'Inicio de sesión exitoso', 'user': user_data,'token': token})
    else:
        return jsonify({'message': 'Credenciales inválidas'})
