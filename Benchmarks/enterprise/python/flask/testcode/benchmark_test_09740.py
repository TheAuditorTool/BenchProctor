# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest09740():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
