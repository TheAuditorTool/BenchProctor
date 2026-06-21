# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest07524():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    return jsonify({'error': 'An internal error occurred'}), 500
