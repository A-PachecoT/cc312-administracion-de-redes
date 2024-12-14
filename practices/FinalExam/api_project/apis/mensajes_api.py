from flask import Blueprint, request, jsonify
from .db_config import messages_db, check_user_exists

# Crear Blueprint para la API de mensajes
mensajes_bp = Blueprint('mensajes', __name__)

@mensajes_bp.route('/messages/write', methods=['POST'])
def write_message():
    """
    API de Mensajes - Escritura: Guarda un mensaje de un usuario registrado
    """
    data = request.get_json()
    if not data or 'usuario' not in data or 'mensaje' not in data:
        return jsonify({'error': 'Usuario y mensaje son requeridos'}), 400
    
    user = data['usuario']
    message = data['mensaje']
    
    # Primero autenticar al usuario
    if not check_user_exists(user):
        return jsonify({'error': 'Usuario no Registrado'}), 404
    
    # Guardar el mensaje
    messages_db.insert({
        'usuario': user,
        'mensaje': message
    })
    return jsonify({'message': 'Mensaje guardado exitosamente'}), 201

@mensajes_bp.route('/messages/read', methods=['POST'])
def read_messages():
    """
    API de Mensajes - Lectura: Retorna todos los mensajes para usuarios registrados
    """
    data = request.get_json()
    if not data or 'usuario' not in data:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    
    user = data['usuario']
    
    # Primero autenticar al usuario
    if not check_user_exists(user):
        return jsonify({'error': 'Usuario no Registrado'}), 404
    
    # Obtener todos los mensajes
    messages = messages_db.all()
    
    # Formatear la respuesta según el ejemplo
    formatted_messages = []
    for msg in messages:
        formatted_messages.append([msg['usuario'], msg['mensaje']])
    
    return jsonify(formatted_messages), 200
