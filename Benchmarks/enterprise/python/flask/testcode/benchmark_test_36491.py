# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest36491():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
