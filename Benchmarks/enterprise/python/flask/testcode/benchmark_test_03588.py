# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03588():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    int(str(data))
    return jsonify({"result": "success"})
