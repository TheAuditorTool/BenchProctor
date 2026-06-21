# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest28398():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
