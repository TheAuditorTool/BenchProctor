# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import hashlib
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12358(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return jsonify({'error': 'integrity check failed'}), 502
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
