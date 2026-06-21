# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00199():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
