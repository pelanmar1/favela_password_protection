from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
import one_class_svm
app = Flask(__name__)

@app.route("/")
def home():
    file = open("log.txt", "a")
    file.write("GOT HOME")
    file.close()
    return "hi"
@app.route("/index")

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        one_class_svm.train()
        prediction = one_class_svm.test()
        file = open("log.txt", "a")
        file.write("GOT POST")
        file.close()
        datafromjs = request.form['mydata']
        result = "return this"
        resp = make_response('{"response": '+str(prediction)+'}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        return render_template('login.html', message='')

if __name__ == "__main__":
    app.run(debug = True)