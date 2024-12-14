from flask import Blueprint, request, jsonify
from .db_config import users_db, Query

# Crear Blueprint para la API de registro
registro_bp = Blueprint('registro', __name__)

@registro_bp.route('/register', methods=['POST'])
def register():
    """
    API de Registro: Recibe un usuario y lo registra en la base de datos
    """
    data = request.get_json()
    if not data or 'usuario' not in data:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    
    user = data['usuario']
    User = Query()
    
    # Verificar si el usuario ya existe
    if users_db.search(User.usuario == user):
        return jsonify({'error': 'Usuario ya existe'}), 400
    
    # Registrar nuevo usuario
    users_db.insert({'usuario': user})
    return jsonify({'message': 'Usuario registrado exitosamente'}), 201
