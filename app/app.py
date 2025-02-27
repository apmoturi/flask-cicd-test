from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    print("Request received at root endpoint", file=sys.stderr)
    return "Hello, Docker!"

if __name__ == '__main__':
    print("Starting Flask application...", file=sys.stderr)
    app.run(host='0.0.0.0', port=5000, debug=True)
