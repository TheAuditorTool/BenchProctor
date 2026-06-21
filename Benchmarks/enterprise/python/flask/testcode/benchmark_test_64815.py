# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest64815():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
