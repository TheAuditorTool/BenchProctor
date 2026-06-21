# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24664():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
