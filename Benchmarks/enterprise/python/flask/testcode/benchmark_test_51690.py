# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest51690():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    return jsonify({'error': 'An internal error occurred'}), 500
