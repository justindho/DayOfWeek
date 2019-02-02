# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:01:04 2019

@author: Justin Ho
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
    
