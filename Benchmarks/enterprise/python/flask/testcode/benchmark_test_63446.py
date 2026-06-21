# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest63446():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    session['user'] = str(data)
    return jsonify({"result": "success"})
