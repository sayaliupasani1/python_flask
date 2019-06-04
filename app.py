from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! Welcome to my page!'

@app.route('/info')
def info():
    return 'This page includes your personal info'

if __name__ == '__main__':
    app.run()
