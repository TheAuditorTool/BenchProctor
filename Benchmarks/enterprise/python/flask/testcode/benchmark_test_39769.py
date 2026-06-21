# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest39769():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
