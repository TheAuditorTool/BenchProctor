# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest08517():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
