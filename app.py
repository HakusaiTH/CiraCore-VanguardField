from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
socketio = SocketIO(app)

object_names = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/endpoint', methods=['POST'])
def receive_data():
    global object_names
    data = request.get_json()
    object_names = data.get('object_names', [])
    
    print(f"Received object names: {object_names}")
    # Emit the new object names to the client
    socketio.emit('update', {'object_names': object_names})
    
    return jsonify({'message': 'Data received successfully', 'object_names': object_names})

if __name__ == '__main__':
    socketio.run(app, debug=True)
