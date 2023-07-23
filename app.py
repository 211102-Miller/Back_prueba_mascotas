from flask import Flask
#from firebase_connection import initialize_firebase
from controllers.user_controller import register as register_user
from controllers.user_controller import login
from controllers.pets_controller import get_form_adopted
from controllers.pets_controller import forms
from utils.jwt_utils import token_required


app = Flask(__name__)



# Rutas
app.route('/register', methods=['POST'])(register_user)
app.route('/login', methods=['POST'])(login)

@app.route('/getAdopted', methods=['GET'])
@token_required
def get_adopted():
    return get_form_adopted()

@app.route('/formAdopted', methods=['POST'])
@token_required
def form_adopted():
    return forms()



if __name__ == '__main__':
    app.run()
