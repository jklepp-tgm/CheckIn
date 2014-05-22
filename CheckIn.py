#!/bin/env python

from flask import Flask
from flask import render_template

app = Flask(__name__)

apipath = u"/v0/"

@app.route("/")
def index():
    return render_template('index.html')

@app.route(apipath + "/FileList")
def filelist():
    pass

# start webservice
if __name__ == "__main__":
    app.run('0.0.0.0')
