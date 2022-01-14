from flask import Flask
import pandas as pd

print('outside function')

app = Flask(__name__)


@app.route('/home')
def printHi():
    return 'hello'


app.run()


def lambda_handler(event, context):
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done!!!!!!!!!!!!!!!!!')
