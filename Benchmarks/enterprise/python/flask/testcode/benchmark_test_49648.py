# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest49648():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
