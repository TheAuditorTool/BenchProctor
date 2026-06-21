# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest67966():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = RequestPayload(forwarded_ip).value
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
