# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest21585():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
