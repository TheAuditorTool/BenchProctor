# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest73242():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
