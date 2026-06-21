# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest15020():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
