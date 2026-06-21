# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest54072():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
