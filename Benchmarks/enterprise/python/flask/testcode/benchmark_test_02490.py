# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02490():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = RequestPayload(file_value).value
    auth_check('user', data)
    return jsonify({"result": "success"})
