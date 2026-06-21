# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest23451():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    session['data'] = str(data)
    return jsonify({"result": "success"})
