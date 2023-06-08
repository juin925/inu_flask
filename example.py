from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello'

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug=True)