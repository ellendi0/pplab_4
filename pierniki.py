from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/api/v1/hello-world-9')
def danone():
    return "<h1>Hello world 9!</h1>"
serve(app, host='localhost', port=5000, threads=1)