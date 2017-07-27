from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from flask import jsonify
from flask import json
import ast
import one_class_svm
import json
import one_class_svm

app = Flask(__name__)
training_set = []

@app.route("/")
def home():
    file = open("log.txt", "a")
    file.write("GOT HOME")
    file.close()
    return "hi"

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        features = json.dumps(request.get_json(force=True)['features'])
        features = ast.literal_eval(features)
        training_set.append(list(features))
        file = open("log.txt", "a")
        file.write(str(training_set))
        file.close()
        return 'Training Sample Added'

@app.route('/train', methods=['GET', 'POST'])
def trainMethod():
    message = None
    if request.method == 'GET':
        one_class_svm.train(training_set)
        return "Data trained"

@app.route('/test', methods=['GET', 'POST'])
def testMethod():
    if request.method == 'POST':
        response = 'Training set is empty.'
        if len(training_set)>0:
            features = json.dumps(request.get_json(force=True)['features'])
            features = ast.literal_eval(features)
            response = str(one_class_svm.test(features))
        return response

@app.route('/clean', methods=['GET', 'POST'])
def cleanMethod():
    if(request.method =='GET'):
        while len(training_set)>0:
            training_set.pop()
        file = open("log.txt", "a")
        file.write("GOT HERE")
        file.close()
        return 'Training set cleaned'

@app.route('/checkset', methods=['GET', 'POST'])
def checkTrainingSet():
    return str(training_set)  

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == "__main__":
    app.run(debug = True)