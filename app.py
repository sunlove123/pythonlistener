from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/canvas', methods=['POST'])
def setup():
    data = json.loads(request.data.decode('utf-8'))
    print request.data
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000', debug=True)
