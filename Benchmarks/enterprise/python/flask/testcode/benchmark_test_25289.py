# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest25289():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
