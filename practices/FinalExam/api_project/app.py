from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
import os

app = Flask(__name__)

# Initialize databases
db_path = 'db'
if not os.path.exists(db_path):
    os.makedirs(db_path)

users_db = TinyDB(os.path.join(db_path, 'users.json'))
messages_db = TinyDB(os.path.join(db_path, 'messages.json'))

# API 1: Registration API
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'usuario' not in data:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    
    user = data['usuario']
    User = Query()
    
    # Check if user already exists
    if users_db.search(User.usuario == user):
        return jsonify({'error': 'Usuario ya existe'}), 400
    
    # Register new user
    users_db.insert({'usuario': user})
    return jsonify({'message': 'Usuario registrado exitosamente'}), 201

# API 2: Authentication API
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    if not data or 'usuario' not in data:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    
    user = data['usuario']
    User = Query()
    
    # Check if user exists
    if users_db.search(User.usuario == user):
        return jsonify({'message': 'Ok'}), 200
    return jsonify({'message': 'Usuario no Registrado'}), 404

# Helper function to check if user exists
def check_user_exists(username):
    User = Query()
    return users_db.search(User.usuario == username)

# API 3: Message Box API
@app.route('/messages/write', methods=['POST'])
def write_message():
    data = request.get_json()
    if not data or 'usuario' not in data or 'mensaje' not in data:
        return jsonify({'error': 'Usuario y mensaje son requeridos'}), 400
    
    user = data['usuario']
    message = data['mensaje']
    
    # First authenticate the user
    if not check_user_exists(user):
        return jsonify({'error': 'Usuario no Registrado'}), 404
    
    # Save the message
    messages_db.insert({
        'usuario': user,
        'mensaje': message
    })
    return jsonify({'message': 'Mensaje guardado exitosamente'}), 201

@app.route('/messages/read', methods=['POST'])
def read_messages():
    data = request.get_json()
    if not data or 'usuario' not in data:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    
    user = data['usuario']
    
    # First authenticate the user
    if not check_user_exists(user):
        return jsonify({'error': 'Usuario no Registrado'}), 404
    
    # Get all messages
    messages = messages_db.all()
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000) 