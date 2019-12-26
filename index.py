#!/usr/bin/env python
""" test"""

from flask import Flask, render_template
APP = Flask(__name__)

@APP.route('/')
def hello():
    """Affiche Helleo"""

    return render_template("home.html", message="Hello Amadou, Welcome in your favorite page!")

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
