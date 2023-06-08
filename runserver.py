from flask import Flask, request, render_template, redirect, jsonify
import runfile as rf
import subprocess

results = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    img = []
    global results
    for i in range(1, 4):
        data = request.form[f'message{i}']
        img.append(data)
    
    results = rf.yolo(img)
    img = []
    return redirect('/results')

@app.route('/results', methods = ['POST', 'GET'])
def results():
    global results
    return results

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug=True)


