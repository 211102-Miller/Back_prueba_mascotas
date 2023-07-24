# jwt_utils.py
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

from dotenv import dotenv_values

# Cargar las variables de entorno desde el archivo .env
env_variables = dotenv_values('venv/.env_todo')

# Obtener el valor de una variable de entorno específica, por ejemplo, "DATABASE_URL"
clave = env_variables.get('CLAVE_JWT')

print(clave)



def generate_token(user_id):
    # Define la fecha de expiración del token (1 hora desde ahora)
    expiration_date = datetime.utcnow() + timedelta(hours=1)

    # Crea el payload del token con el ID del usuario y la fecha de expiración
    payload = {
        'user_id': user_id,
        'exp': expiration_date
    }

    # Genera el token JWT firmado con la clave secreta
    token = jwt.encode(payload, clave, algorithm='HS256')

    return token

def verify_token(token):
    try:
        # Decodifica el token JWT y verifica la firma utilizando la clave secreta
        payload = jwt.decode(token, clave, algorithms=['HS256'])
        user_id = payload['user_id']
        return user_id
    except jwt.ExpiredSignatureError:
        # El token ha expirado
        return None
    except jwt.InvalidTokenError:
        # El token es inválido
        return None
# Decorador para verificar el token JWT

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Verificar si el token se envía en la cabecera de autorización
        if 'Authorization' in request.headers:
            # Obtener el token de la cabecera
            token = request.headers['Authorization'].split(' ')[1]

        if not token:
            return jsonify({'message': 'Token de acceso faltante'}), 401

        try:
            # Decodificar y verificar el token
            payload = jwt.decode(token, clave, algorithms=['HS256'])
            # Aquí puedes realizar validaciones adicionales según tus necesidades

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token de acceso expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token de acceso inválido'}), 401

        # Ejecutar la función de la ruta
        return f(*args, **kwargs)

    return decorated