#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for
import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Canvas Technology!!!\n"

@app.route('/canvas', methods=['POST'])
def setup():
    try:
        data = json.loads(request.data.decode('utf-8'))
        tag = data['push_data']['tag']
        print tag
        #subprocess.check_output("cp /home/ubuntu/canvas_template/test.sh /home/ubuntu/python_service/", shell=True)
        subprocess.check_output("cp /home/ubuntu/yaml/* /home/ubuntu/kube_yaml/", shell=True)
        print 'template copied'
        subprocess.check_output("sed -i 's/{rev}/'"+tag+"'/g' /home/ubuntu/kube_yaml/*", shell=True)
        print 'Revision ID updated'
        subprocess.call(['/home/ubuntu/python_service/kube.sh'])
        print 'KubeOperations!!!!'
        return "ok"
    except Exception as e:
        print "Exception Occured"
        return "Required a valid JSON which fits in the business requirement\n"

app.run(host='0.0.0.0',port='5000', debug=True)
