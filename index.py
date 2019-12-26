""" ceci est un test flask"""

from flask import Flask
app = Flask(__name__)

@App.route('/')
def hello():
    """Affiche Helleo"""

    return "Hello World!"

if __name__ == "__main__":
    """main fucntion"""
    App.run(host="0.0.0.0", port=5000)
