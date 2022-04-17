from flask import Flask
app = Flask(__name__)

# should come from environment variables to ensure real security
app.config['SECRET_KEY'] = 'fweiujfbweiubvfeiw'

# import everything from routes (needs to be after the app is instantiated)
from routes import *

if __name__ == '__main__':
    app.run(debug=True)