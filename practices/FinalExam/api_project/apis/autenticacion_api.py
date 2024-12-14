from flask import Blueprint, request, jsonify
from .db_config import check_user_exists

# Crear Blueprint para la API de autenticación
autenticacion_bp = Blueprint('autenticacion', __name__)

@autenticacion_bp.route('/authenticate', methods=['POST'])
def authenticate():
    """
    API de Autenticación: Verifica si un usuario está registrado
    """
    data = request.get_json()
    if not data or 'usuario' not in data:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    
    user = data['usuario']
    
    # Verificar si el usuario existe
    if check_user_exists(user):
        return jsonify({'message': 'Ok'}), 200
    return jsonify({'message': 'Usuario no Registrado'}), 404
