from flask import Flask, jsonify
import os

# Create Flask app
app = Flask(__name__)

# Get port from environment variable or default to 3333
PORT = int(os.environ.get('PORT', 3333))

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "port": PORT
    })

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello, CI/CD!",
        "server_port": PORT
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
