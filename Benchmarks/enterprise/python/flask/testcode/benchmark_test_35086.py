# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from flask import session


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest35086():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
