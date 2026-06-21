# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import hashlib
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest72571():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return jsonify({'error': 'integrity check failed'}), 502
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
