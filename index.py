#!/usr/bin/env python
""" test"""

from flask import Flask, request, render_template
APP = Flask(__name__)

@APP.route('/')
def hello():
    """Affiche Helleo"""

    return render_template("home.html")

@APP.route('/', methods=['POST'])
def text_box():
    """ method post"""
    text = request.form['text']
    processed_text = text.upper()
    return render_template("page_suivante.html", message=processed_text)

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
