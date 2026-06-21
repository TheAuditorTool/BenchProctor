# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest42952():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
