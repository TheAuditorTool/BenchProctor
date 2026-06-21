# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest09841():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
