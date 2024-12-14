from tinydb import TinyDB, Query
import os

# Inicializar directorio de base de datos
db_path = 'db'
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Bases de datos compartidas
users_db = TinyDB(os.path.join(db_path, 'users.json'))
messages_db = TinyDB(os.path.join(db_path, 'messages.json'))

# Función de utilidad para verificar existencia de usuario
def check_user_exists(username):
    User = Query()
    return users_db.search(User.usuario == username)
