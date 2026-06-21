# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest26503():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
