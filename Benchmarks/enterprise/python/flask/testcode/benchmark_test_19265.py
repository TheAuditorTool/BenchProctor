# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest19265():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
