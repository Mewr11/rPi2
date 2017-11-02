'''
Run this test program each time you start up your virtualenv environment.

Please refer to README.md for instructions on how to set up virtualenv.
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
