from flask import Flask
app = Flask(__name__)


@app.route('/home')
def printHi():
    return 'hello'


app.run()
