#!/bin/env python

import default_config as config

from flask import abort
from flask import Flask
from flask import json
from flask import jsonify
from flask import render_template
from flask import request
from flask import Response

import os

from pathlib import Path

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/FileList")
def filelist():
    root_path = Path(config.document_root)
    try:
        p = root_path / request.args['path']
    except:
        p = root_path

    if p.resolve() < root_path.resolve():
        abort(403)

    return Response(json.dumps([{
        "name": os.path.basename(str(x)),
        "isDirectory": x.is_dir()}
        for x in p.iterdir()]), mimetype='application/json')

# start webservice
if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')
