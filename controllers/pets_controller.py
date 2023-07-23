from firebase_connection import db_firestore
from flask import request, jsonify, render_template
from models.pets_models import FormAdoptedModel

def get_form_adopted():
    # Obtener una referencia a la colección "FormAdopted"
    form_adopted_ref = db_firestore.collection('FormAdopted')
    
    # Obtener todos los documentos de la colección
    documents = form_adopted_ref.get()
    
    # Crear una lista para almacenar los datos
    data = []
    
    # Recorrer los documentos y agregar sus datos a la lista
    for doc in documents:
        data.append(doc.to_dict())
    
    # Devolver los datos en formato JSON
    return jsonify(data)


def forms():
    nombre = request.form['nombre']
    raza = request.form['raza']
    image = request.files['image']
    horario = request.form['horario']
    ubicacion = request.form['ubicacion']

    form_model = FormAdoptedModel()
    document_id = form_model.save_form_data(nombre, raza, image, horario, ubicacion)
    
    # Devolver una respuesta JSON con el ID del documento
    return jsonify({'document_id': document_id})

