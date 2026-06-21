# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest05321():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    auth_check('user', data)
    return jsonify({"result": "success"})
