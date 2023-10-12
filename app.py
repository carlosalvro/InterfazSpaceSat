from flask import Flask, render_template
from flask_serial import Serial
from flask_socketio import SocketIO
from rutas import CansatApp
import re
import json

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config.from_object("config")

ser = Serial(app)
socketio = SocketIO(app)

app.register_blueprint(CansatApp)

# @app.route('/')
# def index():
#     return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('Cliente conectado')

@socketio.on('disconnect')
def test_disconnect():
    print('Cliente desconectado')

@ser.on_message()
def handle_message(msg):
    data = msg.decode('utf-8')
    data = data.strip('\r\n')
    print("receive a message:", data, check_chunk_complete(data))
    if check_chunk_complete(data):
      data = json.loads(data)
      socketio.emit("arduino_data", data)

@socketio.on('send_message')
def prueba(data):
    print(data)


def check_chunk_complete(chunk):
    expr = r'\{("..":"\d+",*){1,}\}'
    if re.match(expr, chunk):
      return True
    else: return False



if __name__ == '__main__':
    # Inicia la aplicación Flask-SocketIO
    socketio.run(app, debug=False)