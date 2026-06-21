# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest74682():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
