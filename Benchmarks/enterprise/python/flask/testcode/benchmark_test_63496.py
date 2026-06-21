# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest63496():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    auth_check('user', data)
    return jsonify({"result": "success"})
