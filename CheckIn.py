#!/bin/env python

from flask import Flask
from flask import Response
from flask import render_template

from pathlib import Path

import json

import default_config as config

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/FileList")
def filelist():
    p = Path(config.document_root)
    return Response(json.dumps([{
        "name": str(x),
        "isDirectory": x.is_dir()}
        for x in p.iterdir()]), mimetype='application/json')

# start webservice
if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')
