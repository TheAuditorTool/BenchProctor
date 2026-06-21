# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest55085():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
