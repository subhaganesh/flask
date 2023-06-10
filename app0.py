from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    return 'welcome to flask'

@app.route('/flask')
def intro():
    return 'flask is used for deployment'

if __name__ == '__main__':
    app.run()
