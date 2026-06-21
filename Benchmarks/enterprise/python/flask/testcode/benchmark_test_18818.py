# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest18818():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
