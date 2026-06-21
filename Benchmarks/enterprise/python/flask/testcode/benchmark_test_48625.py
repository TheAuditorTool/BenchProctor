# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest48625():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
