from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join("/home/administrator/test/", filename))
    return 'ok'

app.run(host='0.0.0.0', port='5000', debug=True)
