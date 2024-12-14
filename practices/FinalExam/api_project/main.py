from flask import Flask
from apis.registro_api import registro_bp
from apis.autenticacion_api import autenticacion_bp
from apis.mensajes_api import mensajes_bp
import requests
import json
import time

app = Flask(__name__)

# Registrar los blueprints de las APIs
app.register_blueprint(registro_bp)
app.register_blueprint(autenticacion_bp)
app.register_blueprint(mensajes_bp)

def ejecutar_demo():
    """
    Función que ejecuta el demo según el ejemplo proporcionado
    """
    base_url = 'http://localhost:5000'
    
    print("\n=== Iniciando Demo de APIs ===\n")
    
    # Registrar usuario "uni"
    print('Cliente: Registrar("uni")')
    response = requests.post(f'{base_url}/register', json={'usuario': 'uni'})
    print(f"Respuesta: {response.json()}\n")
    
    # Autenticar usuario "uni"
    print('Cliente: Autenticar("uni")')
    response = requests.post(f'{base_url}/authenticate', json={'usuario': 'uni'})
    print(f'Respuesta: "{response.json()["message"]}"\n')
    
    # Autenticar usuario no registrado "fc"
    print('Cliente: Autenticar("fc")')
    response = requests.post(f'{base_url}/authenticate', json={'usuario': 'fc'})
    print(f'Respuesta: "{response.json()["message"]}"\n')
    
    # Registrar usuario "fc"
    print('Cliente: Registrar("fc")')
    response = requests.post(f'{base_url}/register', json={'usuario': 'fc'})
    print(f"Respuesta: {response.json()}\n")
    
    # Escribir mensajes
    print('Cliente: Escribir("uni","Este es un mensaje")')
    requests.post(f'{base_url}/messages/write', 
                 json={'usuario': 'uni', 'mensaje': 'Este es un mensaje'})
    
    print('Cliente: Escribir("uni","Este es un segundo mensaje")')
    requests.post(f'{base_url}/messages/write', 
                 json={'usuario': 'uni', 'mensaje': 'Este es un segundo mensaje'})
    
    print('Cliente: Escribir("fc","Tercer mensaje")')
    requests.post(f'{base_url}/messages/write', 
                 json={'usuario': 'fc', 'mensaje': 'Tercer mensaje'})
    
    print('Cliente: Escribir("faua","Otro mensaje")')
    response = requests.post(f'{base_url}/messages/write', 
                           json={'usuario': 'faua', 'mensaje': 'Otro mensaje'})
    print(f"Respuesta: {response.json()}\n")
    
    # Leer todos los mensajes
    print('Cliente: LeerTodo("uni")')
    response = requests.post(f'{base_url}/messages/read', json={'usuario': 'uni'})
    print("Respuesta:")
    for usuario, mensaje in response.json():
        print(f'"{usuario}","{mensaje}"')
    print()

if __name__ == '__main__':
    # Iniciar el servidor en un hilo separado
    import threading
    server = threading.Thread(target=app.run, kwargs={'debug': False, 'port': 5000})
    server.daemon = True
    server.start()
    
    # Esperar un momento para que el servidor inicie
    time.sleep(2)
    
    # Ejecutar el demo
    ejecutar_demo() 