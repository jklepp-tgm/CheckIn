#!/bin/env python

import default_config as config

from flask import Flask
from flask import Response
from flask import render_template
from flask import request

import json

import os

from pathlib import Path

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/FileList")
def filelist():
    try:
        p = Path(request.args['path'])
    except:
        p = Path(config.document_root)

    return Response(json.dumps([{
        "name": os.path.basename(str(x)),
        "isDirectory": x.is_dir()}
        for x in p.iterdir()]), mimetype='application/json')

# start webservice
if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')
