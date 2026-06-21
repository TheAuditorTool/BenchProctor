# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest20686():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    return jsonify({'error': 'An internal error occurred'}), 500
